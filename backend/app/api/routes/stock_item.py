from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.exceptions import ConflictError

from app.core.database import get_db
from app.schemas.stock_item import (
    StockItemCreate,
    StockItemDetailResponse,
    StockItemResponse,
)
from app.services.stock_item_service import (
    create_stock_item_service,
    get_low_stock_items_service,
    get_stock_items_service,
)

router = APIRouter(
    prefix="/stock-items",
    tags=["Stock Items"],
)


@router.post(
    "",
    response_model=StockItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_stock_item(
    stock_item_data: StockItemCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_stock_item_service(db, stock_item_data)

    except ConflictError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        )


@router.get(
    "/low-stock",
    response_model=list[StockItemDetailResponse],
)
def get_low_stock_items(
    db: Session = Depends(get_db),
):
    return get_low_stock_items_service(db)


@router.get(
    "",
    response_model=list[StockItemDetailResponse],
)
def get_stock_items(
    db: Session = Depends(get_db),
):
    return get_stock_items_service(db)
