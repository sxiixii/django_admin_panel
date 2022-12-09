# Спринт 2
 
## Проект `django_api`

### Установка:
1. Перейти в каталог с проектом `/app` и переименовать файл `.env.template` в `.env` и заполнить переменными окружения согласно шаблону
2. Перейти в корневую директорию и начать билд и запуск контейнеров
    `docker compose up`
    У вас должен быть установлен [докер](https://docs.docker.com/engine/install/)
3. После запуска контейнеров можно наполнить БД данными. Для этого выполнить ряд команд из корневой директории:
   `make fake_migrate` - создаст фэйковую инит-миграцию для приложения movies
   `make migrate` - ини-миграции для стандартных приложений Django (admin, sessions, etc)
   `make fixture` - загрузит дамп БД в контейнер из папки fixtures
   `make superuser` - создаст суперпользователя. Предложит заполнить данные в интерактивном режиме
