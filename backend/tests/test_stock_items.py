from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app
from tests.utils import create_product, create_stock_item, create_stock_location

client = TestClient(app)


def setup_stock_item_test_data():
    unique_id = uuid4().hex[:8]

    product = create_product(client, sku=f"TEST-STOCK-ITEM-{unique_id}")

    location = create_stock_location(
        client,
        name=f"Test Stock Item Location {unique_id}",
        location_type="internal",
    )

    return product, location


def test_get_stock_items_returns_200():
    response = client.get("/api/stock-items")

    assert response.status_code == 200


def test_get_stock_items_returns_list():
    response = client.get("/api/stock-items")

    data = response.json()

    assert isinstance(data, list)


def test_create_stock_item_returns_201():
    product, location = setup_stock_item_test_data()

    response = client.post(
        "/api/stock-items",
        json={
            "product_id": product["id"],
            "location_id": location["id"],
            "quantity": 5,
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["product_id"] == product["id"]
    assert data["location_id"] == location["id"]
    assert data["quantity"] == 5
    assert "id" in data


def test_create_stock_item_returns_409_for_duplicate():
    product, location = setup_stock_item_test_data()

    create_stock_item(
        client,
        product_id=product["id"],
        location_id=location["id"],
        quantity=0,
    )

    response = client.post(
        "/api/stock-items",
        json={
            "product_id": product["id"],
            "location_id": location["id"],
            "quantity": 0,
        },
    )

    assert response.status_code == 409
    assert (
        response.json()["detail"]
        == "Stock item already exists for this product and location"
    )


def test_create_stock_item_returns_422_for_invalid_quantity():
    product, location = setup_stock_item_test_data()

    response = client.post(
        "/api/stock-items",
        json={
            "product_id": product["id"],
            "location_id": location["id"],
            "quantity": -1,
        },
    )

    assert response.status_code == 422
