from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_stock_items_returns_200():
    response = client.get("/api/stock-items")

    assert response.status_code == 200


def test_get_stock_items_returns_list():
    response = client.get("/api/stock-items")

    data = response.json()

    assert isinstance(data, list)


def test_create_stock_item_returns_409_for_duplicate():
    response = client.post(
        "/api/stock-items",
        json={
            "product_id": 1,
            "location_id": 1,
            "quantity": 0,
        },
    )

    assert response.status_code == 409


def test_create_stock_item_returns_422_for_invalid_quantity():
    response = client.post(
        "/api/stock-items",
        json={
            "product_id": 1,
            "location_id": 1,
            "quantity": -1,
        },
    )

    assert response.status_code == 422
