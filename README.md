# it-solutions
тестовое задание для IT-SOLUTIONS
реализация модели ДДС.   
для визуализации представлена обычная админка django

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Команда проекта](#команда-проекта)

## Технологии
- [Django](https://www.djangoproject.com/) 

## Использование
 1. Склонируйте репозиторий: 
     ```sh
     git clone https://github.com/testtasks-afk/it-solutions.git
     cd it-solutions
     ```
 2. Создайте и активируйте виртуальное окружение: 
     ```sh
     python3 -m venv .venv
     .venv/Scripts/activate
    ```
 3. Установите необходимые зависимости:  	
    ```sh
    pip install -r requirements.txt
    ```
 4. Проведите миграции данных
    ```sh
    python manage.py migrate
    ```
 5. В папке scripts/constants создайте файл .env. Шаблон файла: 
    ```python
    DJANGO_SECRET="your_django_secret"
    ```
 6. Создайте суперпользователя командой 
    ```sh
    python manage.py createsuperuser 
    ```
 7. Запустите сервер:
    ```sh
     python manage.py runserver
     ```

## Команда проекта

- [Шелевой Ярослав](https://github.com/yshelev) — Backend developer

