import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.database import Base
from app.models import URL

# replace database URL with db credentials
TEST_DATABASE_URL = "postgresql+asyncpg://user:password@localhost/test_url_shortener"

test_engine = create_async_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)

@pytest.fixture
async def test_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
def override_get_db():
    async def _override_get_db():
        async with TestingSessionLocal() as session:
            yield session
    return _override_get_db

@pytest.fixture
def test_app(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    return app

@pytest.mark.asyncio
async def test_create_url(test_app, test_db):
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        response = await ac.post("/shorten", json={"target_url": "https://example.com"})

    assert response.status_code == 200

    assert "short_url" in response.json()

@pytest.mark.asyncio
async def test_get_url(test_app, test_db):
    # create url
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        create_response = await ac.post("/shorten", json={"target_url": "https://example.com"})
        short_key = create_response.json()["short_url"]

        # get request to shortkey endpoint
        get_response = await ac.get(f"/{short_key}")

    assert get_response.status_code == 200

    assert get_response.json()["url"] == "https://example.com"

@pytest.mark.asyncio
async def test_get_url_stats(test_app, test_db):
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        create_response = await ac.post("/shorten", json={"target_url": "https://example.com"})
        short_key = create_response.json()["short_url"]

        # get request to stats endpoint
        stats_response = await ac.get(f"/stats/{short_key}")

    assert stats_response.status_code == 200

    assert stats_response.json()["clicks"] == 0

    assert stats_response.json()["original_url"] == "https://example.com"