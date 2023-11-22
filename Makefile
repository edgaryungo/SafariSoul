.PHONY: build
build:
	docker-compose up --build

.PHONY: up
up:
	docker-compose up

.PHONY: down
down:
	docker-compose down

.PHONY: migrations
migrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"


.PHONY: migrate
migrate:
	docker-compose run --rm app sh -c "python manage.py migrate"

.PHONY: startapp
startapp:
	docker-compose run --rm app sh -c "python manage.py startapp $(name)"

.PHONY: createsuperuser
createsuperuser:
	docker-compose run --rm app sh -c "python manage.py createsuperuser"
