from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError
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


@router.post(
    "",
    response_model=StockLocationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_stock_location(
    location_data: StockLocationCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_stock_location_service(db, location_data)

    except ConflictError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        )


@router.get("", response_model=list[StockLocationResponse])
def get_stock_locations(
    db: Session = Depends(get_db),
):
    return get_stock_locations_service(db)
