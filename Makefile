# Development helpers

.PHONY: build up down logs shell

build:
	docker-compose build

up:
	docker-compose up --build -d

down:
	docker-compose down

logs:
	docker-compose logs -f

shell:
	docker-compose exec web /bin/bash
