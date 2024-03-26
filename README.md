# :flower_playing_cards: Асинхронный анализатор поиска работы

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=yellow&labelColor=1e293b)](https://www.python.org/)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)
[![Aiohttp](https://img.shields.io/badge/Aiohttp-3.9-red?style=flat&logo=aiohttp&labelColor=1e293b)](https://docs.aiohttp.org/en/stable/index.html)
[![Tqdm](https://img.shields.io/badge/Tqdm-4.66-orange?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU%2BdHFkbTwvdGl0bGU%2BPHBhdGggZD0iTTEyIDE0LjU2MmEyLjMzOCAyLjMzOCAwIDEgMSAwLTQuNjc3IDIuMzM4IDIuMzM4IDAgMCAxIDAgNC42Nzd6TTEyIDBDNS4zOTIgMCAuMDM2IDUuNDczLjAzNiAxMi4yMjRjMCA1LjU3OSAzLjY1OSAxMC4yODEgOC42NTggMTEuNzQ2LjQyOC4xMjYuODctLjE2Mi45NjItLjU5OGwuMTQxLS42NjljLjA4Ni0uNDEtLjE2OS0uNzk5LS41Ny0uOTItNC4wMzktMS4yMjEtNi45ODYtNS4wMzctNi45ODYtOS41NTkgMC01LjUwNyA0LjM3LTkuOTcyIDkuNzYtOS45NzJzOS43NiA0LjQ2NCA5Ljc2IDkuOTcyYzAgNC41MTUtMi45MzggOC4zMjUtNi45NjcgOS41NTItLjQuMTIyLS42NTQuNTExLS41NjcuOTE5bC4xNDIuNjdjLjA5My40MzcuNTM1LjcyMy45NjMuNTk2IDQuOTg2LTEuNDc0IDguNjMzLTYuMTY5IDguNjMzLTExLjczOEMyMy45NjQgNS40NzMgMTguNjA4IDAgMTIgMHptNy4xNTIgMTIuMjI0YzAtNC4wNC0zLjIwMi03LjMxNS03LjE1Mi03LjMxNXMtNy4xNTIgMy4yNzUtNy4xNTIgNy4zMTVjMCAzLjE5MSAxLjk5OSA1LjkwMyA0Ljc4NiA2LjkwMmEuNzkuNzkgMCAwIDAgMS4wMzctLjU4MmwuMDQyLS4xOTlhLjc3Mi43NzIgMCAwIDAtLjQ4OS0uODg5Yy0yLjExOC0uNzUyLTMuNjM5LTIuODA5LTMuNjM5LTUuMjMyIDAtMy4wNTkgMi40MjQtNS41MzkgNS40MTUtNS41MzlzNS40MTUgMi40OCA1LjQxNSA1LjUzOWMwIDIuNDE4LTEuNTE2IDQuNDcyLTMuNjI4IDUuMjI3YS43NzIuNzcyIDAgMCAwLS40ODcuODlsLjA0Mi4xOTlhLjc5MS43OTEgMCAwIDAgMS4wMzguNThjMi43OC0xLjAwMyA0Ljc3Mi0zLjcxIDQuNzcyLTYuODk2eiIvPjwvc3ZnPg%3D%3D&labelColor=1e293b)](https://tqdm.github.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2-yellow?style=flat&logo=pandas&labelColor=1e293b)](https://pandas.pydata.org/pandas-docs/stable/index.html)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-purple?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjgiIGhlaWdodD0iMTI4IiBzdHJva2U9IiM3NzciIGZpbGwtb3BhY2l0eT0iLjgiPgo8cGF0aCBmaWxsPSIjRkZGIiBkPSJtNjMsMWE2Myw2MyAwIDEsMCAyLDB6bTAsMTRhNDksNDkgMCAxLDAgMiwwem0wLDE0YTM1LDM1IDAgMSwwCjIsMHptMCwxNGEyMSwyMSAwIDEsMCAyLDB6bTAsMTRhNyw3IDAgMSwwIDIsMHptNjQsN0gxbTEwOC00NS05MCw5MG05MCwwLTkwLTkwbTQ1LTE4djEyNiIvPgo8cGF0aCBmaWxsPSIjRjYwIiBkPSJtNTAsOC0yMCwxMCA2OCw5MiAxMC0xMEw2NCw2NHoiLz4KPHBhdGggZmlsbD0iI0ZDMCIgZD0ibTE3LDUwdjI4TDY0LDY0eiIvPgo8cGF0aCBmaWxsPSIjN0Y3IiBkPSJtNjQsNjQgNiwzNUg1OHoiLz4KPHBhdGggZmlsbD0iI0NGMyIgZD0ibTY0LDY0IDEzLTQwIDksNXoiLz4KPHBhdGggZmlsbD0iIzA0RiIgZD0ibTY0LDY0IDE0LTYgMSw0emwtMjYsMTMgMyw0eiIvPgo8L3N2Zz4%3D&labelColor=1e293b)](https://matplotlib.org/stable/)
---

## 🦋 ***Цель проекта***: 
* Изучение api [hh ru](https://github.com/hhru/api)
* Отработка навыков  веб скрапинга 
* Практика написания асинхронного кода
* Визуализировать график
---
### :wilted_flower: ***Описание***
Анализатор  разработан для получения актуальной информации по вакансиям,  сохранением данных в файл и построением   графика.

Проект состоит из 2 основных модулей:
* ```parser.py```
  
    *Модуль* занимается сбором  информации о вакансиях и сохраняет все в  формате ```csv```.
  
    Для старта модуля необходимо:
    *  В функцию  ```gather_data(url=...)``` передать *url*
    *  В терминале выполнить команду ```python parser.py```

    *Процесс работы модуля*
  
    ![vacancy](https://github.com/yakhovets-o/async-vacancy-scraper/assets/112704107/8d8bec65-c2da-4408-beae-526375463e9b)
    
*  ```models.py```

     *Модуль* создает, визуализирует и сохраняет график в формате ```png```.

   
     За основу были взяты ключевые навыки  ```key_skills``` из результата работы модуля ```models```
     и визуализируется ***топ 15*** из них

     Для получения графика:
     * В терминале выполнить команду ```python diagram.py ```
---

*Модуль*  ```models```  хранит  ```pydantic models```

*Модуль*  ```vacancy_gif``` отвечает за создание ```gif``` процесса работы  модуля  ```parser```

---

## :desktop_computer: Установка
#### Для Windows
* Скопируйте репозиторий к себе на компьютер [***async-vacancy-scraper***]([https://github.com/yakhovets-o/job-search-parser.git](https://github.com/yakhovets-o/async-vacancy-scraper.git))
* Установите виртуальное окружение  ```python -m venv venv```
* Активируйте виртуальное окружение ```venv/Scripts/activate```
* Установите внешние библиотеки, выполнив: ```pip install -r requirements.txt```

---

## 🐳 Лицензия 
Данный проект использует

[![MIT](https://img.shields.io/badge/License-MIT-blue)](https://github.com/yakhovets-o/job-search-parser/blob/main/LICENSE)




---
## 🍀 Контакты 

Для связи с автором проекта: 

[![Gmail](https://img.shields.io/badge/-My%20email-%20red?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU%2BR21haWw8L3RpdGxlPjxwYXRoIGQ9Ik0yNCA1LjQ1N3YxMy45MDljMCAuOTA0LS43MzIgMS42MzYtMS42MzYgMS42MzZoLTMuODE5VjExLjczTDEyIDE2LjY0bC02LjU0NS00LjkxdjkuMjczSDEuNjM2QTEuNjM2IDEuNjM2IDAgMCAxIDAgMTkuMzY2VjUuNDU3YzAtMi4wMjMgMi4zMDktMy4xNzggMy45MjctMS45NjRMNS40NTUgNC42NCAxMiA5LjU0OGw2LjU0NS00LjkxIDEuNTI4LTEuMTQ1QzIxLjY5IDIuMjggMjQgMy40MzQgMjQgNS40NTd6Ii8%2BPC9zdmc%2B)](mailto:yakhovetso@gmail.com)



