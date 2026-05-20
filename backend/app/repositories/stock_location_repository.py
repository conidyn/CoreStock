from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError
from app.models.stock_location import StockLocation
from app.schemas.stock_location import StockLocationCreate


def create_stock_location(
    db: Session,
    location_data: StockLocationCreate,
) -> StockLocation:
    location = StockLocation(**location_data.model_dump())

    db.add(location)

    try:
        db.commit()

    except IntegrityError:
        db.rollback()

        raise ConflictError("Stock location already exists")

    db.refresh(location)

    return location


def get_stock_locations(db: Session) -> list[StockLocation]:
    return db.query(StockLocation).all()


def get_stock_location_by_id(
    db: Session,
    location_id: int,
) -> StockLocation | None:
    return db.query(StockLocation).filter(StockLocation.id == location_id).first()
