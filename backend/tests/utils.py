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


def create_stock_movement(
    client: TestClient,
    product_id: int,
    from_location_id: int,
    to_location_id: int,
    quantity: int,
    movement_type: str,
    reason: str,
):
    response = client.post(
        "/api/stock-movements",
        json={
            "product_id": product_id,
            "from_location_id": from_location_id,
            "to_location_id": to_location_id,
            "quantity": quantity,
            "movement_type": movement_type,
            "reason": reason,
        },
    )

    return response
