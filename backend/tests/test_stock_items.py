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


def test_get_low_stock_items_returns_items_below_or_equal_threshold():
    product, location = setup_stock_item_test_data()

    create_stock_item(
        client,
        product_id=product["id"],
        location_id=location["id"],
        quantity=0,
    )

    response = client.get("/api/stock-items/low-stock")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    low_stock_item = next(
        item for item in data if item["product"]["id"] == product["id"]
    )

    assert low_stock_item["quantity"] == 0
    assert low_stock_item["product"]["id"] == product["id"]
    assert low_stock_item["location"]["id"] == location["id"]


def test_get_low_stock_items_excludes_items_above_threshold():
    product, location = setup_stock_item_test_data()

    create_stock_item(
        client,
        product_id=product["id"],
        location_id=location["id"],
        quantity=5,
    )

    response = client.get("/api/stock-items/low-stock")

    assert response.status_code == 200

    data = response.json()

    assert all(item["product"]["id"] != product["id"] for item in data)
