# 🚀 LogiTrack API

![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)

LogiTrack is a **production-grade fleet management and logistics routing API** built with Python and FastAPI. Designed to demonstrate enterprise-level backend architecture with async database operations, containerized deployment, and secure authentication.

## 🌟 Key Features

* **Async-First Architecture:** Built on ASGI with native async/await patterns using `asyncpg` for non-blocking database I/O.
* **Schema Migrations:** Automated database versioning via Alembic, ensuring safe production deployments.
* **JWT Authentication:** Secure token-based auth with role-based access control on sensitive endpoints.
* **Containerized Stack:** Full Docker Compose setup with PostgreSQL, running in isolated containers.
* **Auto-Documentation:** Interactive Swagger UI and ReDoc generated automatically from type-annotated endpoints.
* **Test Suite:** Pytest-based testing infrastructure for endpoint and service layer validation.

## 🏗️ Architecture

```
logitrack-api/
├── app/                    # Application core
│   ├── api/                # Route handlers (controllers)
│   ├── core/               # Config, security, dependencies
│   ├── models/             # SQLAlchemy ORM models
│   ├── schemas/            # Pydantic request/response schemas
│   └── services/           # Business logic layer
├── alembic/                # Database migrations
├── tests/                  # Test suite
├── Dockerfile              # Multi-stage production build
├── docker-compose.yml      # Full stack orchestration
├── Makefile                # Dev automation commands
└── requirements.txt        # Python dependencies
```

## 🛠️ Tech Stack & Architecture

| Layer | Technology |
|-------|-----------|
| **Runtime** | Python 3.12+ |
| **Framework** | FastAPI (ASGI) |
| **ORM** | SQLAlchemy 2.0 (async) |
| **Database** | PostgreSQL 16 + asyncpg |
| **Migrations** | Alembic |
| **Auth** | JWT (python-jose) |
| **Containerization** | Docker & Docker Compose |
| **Testing** | Pytest + httpx |

## 📦 Running Locally

### With Docker (Recommended)

```bash
# Clone and start the full stack
git clone https://github.com/leonardo-gorska/logitrack-api.git
cd logitrack-api

# Copy environment template
cp .env.example .env

# Build and start containers
docker-compose up -d --build
```

### Without Docker

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

## 📚 API Documentation

Once running, access the auto-generated docs:

| Interface | URL |
|-----------|-----|
| **Swagger UI** | [http://localhost:8000/docs](http://localhost:8000/docs) |
| **ReDoc** | [http://localhost:8000/redoc](http://localhost:8000/redoc) |

## 🧪 Testing

```bash
# Run the test suite
pytest

# With coverage
pytest --cov=app tests/
```

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
