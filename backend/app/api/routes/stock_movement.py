from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.exceptions import (
    InvalidLocationTransferException,
    NotFoundError,
    StockInsufficientException,
)

from app.schemas.stock_movement import (
    StockMovementCreate,
    StockMovementResponse,
)
from app.services.stock_movement_service import (
    create_stock_movement_service,
    get_stock_movements_service,
)

router = APIRouter(
    prefix="/stock-movements",
    tags=["Stock Movements"],
)


@router.post(
    "",
    response_model=StockMovementResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_stock_movement(
    movement_data: StockMovementCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_stock_movement_service(db, movement_data)

    except NotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        )

    except StockInsufficientException as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        )

    except InvalidLocationTransferException as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )


@router.get(
    "",
    response_model=list[StockMovementResponse],
)
def get_stock_movements(
    db: Session = Depends(get_db),
):
    return get_stock_movements_service(db)
