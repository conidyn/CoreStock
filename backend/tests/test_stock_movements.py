from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app
from tests.utils import create_product, create_stock_item, create_stock_location

client = TestClient(app)


def setup_stock_movement_test_data(
    source_quantity: int = 10,
    destination_quantity: int = 0,
):
    unique_id = uuid4().hex[:8]

    product = create_product(client, sku=f"TEST-MOVE-{unique_id}")

    source_location = create_stock_location(
        client,
        name=f"Test Source Location {unique_id}",
        location_type="internal",
    )

    destination_location = create_stock_location(
        client,
        name=f"Test Destination Location {unique_id}",
        location_type="internal",
    )

    create_stock_item(
        client,
        product_id=product["id"],
        location_id=source_location["id"],
        quantity=source_quantity,
    )

    create_stock_item(
        client,
        product_id=product["id"],
        location_id=destination_location["id"],
        quantity=destination_quantity,
    )

    return product, source_location, destination_location


def test_create_stock_movement_transfer_returns_201():
    product, source_location, destination_location = setup_stock_movement_test_data()

    response = client.post(
        "/api/stock-movements",
        json={
            "product_id": product["id"],
            "from_location_id": source_location["id"],
            "to_location_id": destination_location["id"],
            "quantity": 3,
            "movement_type": "transfer",
            "reason": "Test transfer movement",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["product_id"] == product["id"]
    assert data["from_location_id"] == source_location["id"]
    assert data["to_location_id"] == destination_location["id"]
    assert data["quantity"] == 3
    assert data["movement_type"] == "transfer"
    assert data["reason"] == "Test transfer movement"
    assert "id" in data
    assert "created_at" in data


def test_create_stock_movement_returns_409_when_stock_is_insufficient():
    product, source_location, destination_location = setup_stock_movement_test_data(
        source_quantity=2,
    )

    response = client.post(
        "/api/stock-movements",
        json={
            "product_id": product["id"],
            "from_location_id": source_location["id"],
            "to_location_id": destination_location["id"],
            "quantity": 999,
            "movement_type": "transfer",
            "reason": "Invalid transfer with insufficient stock",
        },
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Not enough stock available"


def test_create_stock_movement_returns_404_when_source_stock_item_not_found():
    product, _, destination_location = setup_stock_movement_test_data()

    response = client.post(
        "/api/stock-movements",
        json={
            "product_id": product["id"],
            "from_location_id": 999999,
            "to_location_id": destination_location["id"],
            "quantity": 1,
            "movement_type": "transfer",
            "reason": "Invalid transfer with missing source",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Source stock item not found"


def test_create_stock_movement_returns_404_when_destination_stock_item_not_found():
    product, source_location, _ = setup_stock_movement_test_data()

    response = client.post(
        "/api/stock-movements",
        json={
            "product_id": product["id"],
            "from_location_id": source_location["id"],
            "to_location_id": 999999,
            "quantity": 1,
            "movement_type": "transfer",
            "reason": "Invalid transfer with missing destination",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Destination stock item not found"
