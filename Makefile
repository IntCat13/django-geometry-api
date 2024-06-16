init:
	docker-compose down -v
	docker-compose up --build -d
	docker-compose exec web python manage.py makemigrations geo_core
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py test

dev:
	docker-compose down
	docker-compose up --build -d
	docker-compose exec web python manage.py test
	docker-compose logs -f

test:
	docker-compose exec web python manage.py test

deploy:
	docker-compose up --build -d