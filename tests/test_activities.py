import pytest
from httpx import AsyncClient
from src.app import app

@pytest.mark.asyncio
async def test_fetch_activities():
    # Arrange
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Act
        response = await client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)