# LogiTrack API

Sistema corporativo de gerenciamento de frotas e roteamento logístico (LogiTrack). 
Projeto modelo desenvolvido com Python (FastAPI), PostgreSQL (assíncrono) e Docker.

## Stack
- Python 3.12+
- FastAPI
- PostgreSQL + Asyncpg + SQLAlchemy + Alembic
- Docker & Docker Compose
- JWT (JSON Web Tokens)
- Pytest

## Como rodar localmente

Clone o projeto e inicie os containers:

```bash
docker-compose up -d --build
```

Acesse a documentação:
- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
