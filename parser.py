import asyncio
import csv
import logging.config
from typing import NoReturn

import aiofiles
import aiohttp

from aiocsv import AsyncDictWriter, AsyncWriter
from fake_useragent import UserAgent
from tqdm.asyncio import tqdm

from models import Vacancy

ua = UserAgent().random
lock = asyncio.Lock()
headers = {
    'User-Agent': f'{ua}',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
}


async def get_vacancy(session: aiohttp.ClientSession, vacancy_url: str) -> None | NoReturn:
    try:
        async with session.get(url=vacancy_url) as response:

            logger.info(vacancy_url)

            vacancy_json = await response.json()
            vacancy_model = Vacancy.parse_obj(vacancy_json)

            await write_csv(vacancy_model=vacancy_model.get_value())

    except aiohttp.ClientConnectionError as cce:
        logger.error(cce, exc_info=True)
    except Exception as ex:
        logger.error(ex, exc_info=True)


async def gather_data(url: str) -> None | NoReturn:
    try:

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url=url) as response:

                response_json = await response.json()
                page_count = response_json['pages']

                tasks = []

                for page in range(page_count):
                    params = {'page': page}

                    async with session.get(url=url, params=params) as resp:

                        resp_json = await resp.json()
                        vacancies = resp_json['items']

                        # процесс-бар tqdm
                        async for vacancy in tqdm(vacancies, desc='Vacancies', unit=' vacancy', mininterval=.6):
                            await asyncio.sleep(.5)

                            vacancy_url = vacancy['url']
                            task = asyncio.create_task(get_vacancy(session=session, vacancy_url=vacancy_url))
                            tasks.append(task)

                await asyncio.gather(*tasks)
                logging.info("Все загрузки завершены.")

    except aiohttp.ClientConnectionError as cce:
        logger.error(cce, exc_info=True)
    except Exception as ex:
        logger.error(ex, exc_info=True)


async def write_csv(vacancy_model) -> None:
    async with lock:
        async with aiofiles.open(file="vacancy.csv", mode="a", encoding="utf-8", newline="") as afp:
            writer = AsyncDictWriter(afp, fieldnames=['link',
                                                      'job_title',
                                                      'salary',
                                                      'company_name',
                                                      'city',
                                                      'work_experience',
                                                      'work_format',
                                                      'key_skills',
                                                      'publication_date'], restval="NULL", quoting=csv.QUOTE_ALL)

            await writer.writerow(vacancy_model)


async def create_csv() -> None:
    async with aiofiles.open(file='vacancy.csv', mode='w', encoding='utf-8', newline='') as afp:
        writer = AsyncWriter(afp)

        await writer.writerow([
            'link',
            'job_title',
            'salary',
            'company_name',
            'city',
            'work_experience',
            'work_format',
            'key_skills',
            'publication_date'

        ])


async def main() -> None:
    await create_csv()
    await gather_data(url='https://api.hh.ru/vacancies?text=python&area=16&per_page=100')


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)

    asyncio.run(main())


