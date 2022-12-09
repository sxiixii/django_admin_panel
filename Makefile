PROJECT_NAME = Admin_panel

all:
	@echo "make migrate_init		- Выполнить миграции "
	@echo "make fixtures		- Загрузить дамп fixtures.json в БД "
	@echo "make superuser		- Создать суперпользователя "

fake_migrate:
	#Создание фэйковой миграции
	docker compose exec web python manage.py migrate movies --fake

migrate:
	docker compose exec web python manage.py migrate

fixture:
	#Загрузка бэкапа в базу данных.
	docker compose exec web python manage.py loaddata fixtures/dump.json

superuser:
	#Создание суперюзер
	docker compose exec web python manage.py createsuperuser
