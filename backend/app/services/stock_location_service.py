from sqlalchemy.orm import Session

from app.models.stock_location import StockLocation
from app.repositories.stock_location_repository import (
    create_stock_location,
    get_stock_locations,
)
from app.schemas.stock_location import StockLocationCreate


def create_stock_location_service(
    db: Session,
    location_data: StockLocationCreate,
) -> StockLocation:
    return create_stock_location(db, location_data)


def get_stock_locations_service(
    db: Session,
) -> list[StockLocation]:
    return get_stock_locations(db)
