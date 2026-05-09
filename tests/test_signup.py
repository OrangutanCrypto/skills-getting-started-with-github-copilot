import pytest
from httpx import AsyncClient
from src.app import app

@pytest.mark.asyncio
async def test_signup_activity():
    # Arrange
    async with AsyncClient(app=app, base_url="http://test") as client:
        email = "test@mergington.edu"
        activity = "Chess Club"

        # Act
        response = await client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json().get("message") == "Successfully signed up!"