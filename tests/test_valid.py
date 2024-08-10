from app.main import app
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

transport = ASGITransport(app)


@pytest.mark.asyncio
async def test_app():
    async with AsyncClient(transport=transport, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post("/depos", params={
            "date": "30.12.2029",
            "periods": 13,
            "amount": 45678,
            "rate": 4.8,
        })
    assert response.status_code == 200
    assert response.json() == {
        "30.01.2030": 45860.71,
        "28.02.2030": 46044.15,
        "30.03.2030": 46228.33,
        "30.04.2030": 46413.24,
        "30.05.2030": 46598.9,
        "30.06.2030": 46785.29,
        "30.07.2030": 46972.43,
        "30.08.2030": 47160.32,
        "30.09.2030": 47348.97,
        "30.10.2030": 47538.36,
        "30.11.2030": 47728.51,
        "30.12.2030": 47919.43,
        "30.01.2031": 48111.11
    }
