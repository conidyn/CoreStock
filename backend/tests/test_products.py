from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_products_returns_200():
    response = client.get("/api/products")

    assert response.status_code == 200


def test_get_products_returns_list():
    response = client.get("/api/products")

    data = response.json()

    assert isinstance(data, list)
