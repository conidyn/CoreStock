from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.stock_location import (
    StockLocationCreate,
    StockLocationResponse,
)
from app.services.stock_location_service import (
    create_stock_location_service,
    get_stock_locations_service,
)

router = APIRouter(
    prefix="/stock-locations",
    tags=["Stock Locations"],
)


@router.post("", response_model=StockLocationResponse)
def create_stock_location(
    location_data: StockLocationCreate,
    db: Session = Depends(get_db),
):
    return create_stock_location_service(db, location_data)


@router.get("", response_model=list[StockLocationResponse])
def get_stock_locations(
    db: Session = Depends(get_db),
):
    return get_stock_locations_service(db)
