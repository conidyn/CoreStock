from sqlalchemy.orm import Session

from app.models.stock_location import StockLocation
from app.schemas.stock_location import StockLocationCreate


def create_stock_location(
    db: Session,
    location_data: StockLocationCreate,
) -> StockLocation:
    location = StockLocation(**location_data.model_dump())

    db.add(location)
    db.commit()
    db.refresh(location)

    return location


def get_stock_locations(db: Session) -> list[StockLocation]:
    return db.query(StockLocation).all()
