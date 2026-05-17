from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app
from tests.utils import create_product

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
