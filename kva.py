from typing import List
import random
import asyncio
import time
from tqdm.asyncio import trange
import aiofiles


# async def sleep_func(sleep_duration: float = 1) -> float:
#     start_time = time.time()
#     await asyncio.sleep(delay=sleep_duration)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#
#     return elapsed_time
#
#
# async def run_multiple_sleeps(sleep_durations: List[float]) -> List[float]:
#     tasks = []
#     for sleep_duration in sleep_durations:
#         task = asyncio.create_task(sleep_func(sleep_duration=sleep_duration))
#         tasks.append(task)
#
#     actual_sleep_durations = [
#         await f
#         for f in tqdm.tqdm(asyncio.as_completed(tasks), total=len(tasks))
#     ]
#
#     # Alternatively, using tqdm asyncio.as_completed wrapper.
#     # total=len(tasks) now becomes optional.
#     # actual_sleep_durations = [
#     # await f
#     # for f in tqdm.asyncio.tqdm.as_completed(tasks)
#     # ]
#
#     return actual_sleep_durations
#
#
# if __name__ == "__main__":
#     n = 10 ** 5
#     sleep_durations = [random.uniform(0, 5.0) for _ in range(n)]
#
#     actual_sleep_durations = asyncio.run(
#         run_multiple_sleeps(sleep_durations=sleep_durations))

async def csv():
    async with aiofiles.open(file='vacancy.csv', mode='r', encoding='utf-8') as file:
        f = await file.read()

        async for i in trange(f.splitlines(), desc='Pages', unit=' page', colour='red', mininterval=.6):
            await asyncio.sleep(0.2)


if __name__ == "__main__":
    asyncio.run(csv())