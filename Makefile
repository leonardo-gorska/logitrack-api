.PHONY: check build up down logs restart test migrate

check:
	ruff check .
	black --check .

format:
	black .

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f api

restart:
	docker-compose restart api

test:
	docker-compose exec api pytest -v

migrate-create:
	docker-compose exec api alembic revision --autogenerate -m "$(m)"

migrate-up:
	docker-compose exec api alembic upgrade head
