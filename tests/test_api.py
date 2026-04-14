import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.base import Base
from app.api.deps import get_db

# Use an in-memory SQLite database for testing, but since we are heavily relying on PostgreSQL specifics (like UUID),
# we need a test Postgres or to use async sqlite if compatible.
# For industry standard in this demo, let's mock the DB session or use standard SQLite if UUIDs are matched.

# To simplify without mocking the whole DB in this snippet, we setup basic client tests:
@pytest.fixture
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac

@pytest.mark.asyncio
async def test_health_check(async_client: AsyncClient):
    response = await async_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "app": "LogiTrack API"}
