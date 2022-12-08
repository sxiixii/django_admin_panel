# Спринт 2
 
## Проект `docker_compose`

### Установка:
1.  Создать виртуальное окружение в корне проекта удобным способом
    Например:
    `python3 -m venv .venv`
    И активировать его
    `source .venv/bin/activate`
2. Перейти в каталог с проектом `/docker_compose/app` и установить зависимости
    `pip install -r requirements.txt`
3. Переименовать файл `.env.template` в `.env` и заполнить переменными окружения согласно шаблону
4. Для внесение локальных настроек проекта создать файл `dev.py` в директории `docker_compose/app/config/settings/environments/`.
   Настройки базы данных хранятся по пути `docker_compose/app/config/settings/components/database.py`
5. Перейти в каталог `docker_compose` и начать билд и запуск контейнеров
    `docker compose up`
    У вас должен быть установлен [докер](https://docs.docker.com/engine/install/) 
    



## Проект `django_api`

### Установка:

1. Перейти в каталог `django_api`. Для этого проекта можно использовать виртуальное окружение из проекта `docker_compose`, либо создать новое и установить зависимости из файла `requirements.txt`
2. Переименовать файл `.env.template` в `.env` и заполнить переменными окружения согласно шаблону
3. Активировать окружение и запустить сервер Django командой:
    `python manage.py runserver`
4. Для внесение локальных настроек проекта создать файл `dev.py` в директории `django_api/config/settings/environments/`.
   Настройки базы данных хранятся по пути `django_api/config/settings/components/database.py`