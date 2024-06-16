init:
	docker-compose down -v
	docker-compose up --build -d
	docker-compose exec web python manage.py makemigrations geo_core
	docker-compose exec web python manage.py migrate

dev:
	docker-compose up --build

test:
	docker-compose exec web python manage.py test

deploy:
	docker-compose up --build -d
