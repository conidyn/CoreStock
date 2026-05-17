from fastapi.testclient import TestClient


def create_product(
    client: TestClient,
    sku: str,
):
    response = client.post(
        "/api/products",
        json={
            "name": f"Product {sku}",
            "sku": sku,
            "category": "Testing",
            "unit": "pcs",
            "min_stock_threshold": 0,
        },
    )

    return response.json()


def create_stock_location(
    client: TestClient,
    name: str,
    location_type: str,
):
    response = client.post(
        "/api/stock-locations",
        json={
            "name": name,
            "type": location_type,
        },
    )

    return response.json()


def create_stock_item(
    client: TestClient,
    product_id: int,
    location_id: int,
    quantity: int,
):
    response = client.post(
        "/api/stock-items",
        json={
            "product_id": product_id,
            "location_id": location_id,
            "quantity": quantity,
        },
    )

    return response.json()
