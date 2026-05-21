from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_dashboard_stats_returns_200():
    response = client.get("/api/stats/dashboard")

    assert response.status_code == 200


def test_get_dashboard_stats_returns_expected_shape():
    response = client.get("/api/stats/dashboard")

    data = response.json()

    assert "total_products" in data
    assert "total_stock_quantity" in data
    assert "low_stock_count" in data
    assert "total_movements" in data
    assert "movement_breakdown" in data

    assert "purchase" in data["movement_breakdown"]
    assert "transfer" in data["movement_breakdown"]
    assert "sale" in data["movement_breakdown"]
