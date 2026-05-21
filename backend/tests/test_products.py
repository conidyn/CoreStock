from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app
from tests.utils import (
    create_product,
    create_stock_item,
    create_stock_location,
    create_stock_movement,
)

client = TestClient(app)


def test_get_products_returns_200():
    response = client.get("/api/products")

    assert response.status_code == 200


def test_get_products_returns_list():
    response = client.get("/api/products")

    data = response.json()

    assert isinstance(data, list)


def test_create_product_returns_product():
    unique_id = uuid4().hex[:8]

    product = create_product(client, sku=f"TEST-PRODUCT-{unique_id}")

    assert product["sku"] == f"TEST-PRODUCT-{unique_id}"
    assert product["name"] == f"Product TEST-PRODUCT-{unique_id}"
    assert product["category"] == "Testing"
    assert product["unit"] == "pcs"
    assert product["min_stock_threshold"] == 0
    assert "id" in product


def test_create_product_returns_409_for_duplicate_sku():
    unique_id = uuid4().hex[:8]
    sku = f"TEST-DUPLICATE-{unique_id}"

    create_product(client, sku=sku)

    response = client.post(
        "/api/products",
        json={
            "name": "Duplicate product",
            "sku": sku,
            "category": "Testing",
            "unit": "pcs",
            "min_stock_threshold": 0,
        },
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Product SKU already exists"


def test_get_product_movements_returns_product_movements():
    unique_id = uuid4().hex[:8]

    product = create_product(client, sku=f"TEST-PRODUCT-MOVEMENTS-{unique_id}")

    source_location = create_stock_location(
        client,
        name=f"Test Product Movement Source {unique_id}",
        location_type="internal",
    )

    destination_location = create_stock_location(
        client,
        name=f"Test Product Movement Destination {unique_id}",
        location_type="internal",
    )

    create_stock_item(
        client,
        product_id=product["id"],
        location_id=source_location["id"],
        quantity=10,
    )

    create_stock_item(
        client,
        product_id=product["id"],
        location_id=destination_location["id"],
        quantity=0,
    )

    create_stock_movement(
        client=client,
        product_id=product["id"],
        from_location_id=source_location["id"],
        to_location_id=destination_location["id"],
        quantity=3,
        movement_type="transfer",
        reason="Product movement history test",
    )

    response = client.get(f"/api/products/{product['id']}/movements")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["product_id"] == product["id"]
    assert data[0]["quantity"] == 3
    assert data[0]["movement_type"] == "transfer"
    assert data[0]["reason"] == "Product movement history test"
