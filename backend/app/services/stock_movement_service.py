from sqlalchemy.orm import Session

from app.models.stock_movement import StockMovement
from app.repositories.stock_movement_repository import (
    create_stock_movement,
    get_stock_item_by_product_and_location,
    get_stock_movements,
)
from app.schemas.stock_movement import StockMovementCreate
from app.core.exceptions import NotFoundError, StockInsufficientException


def create_stock_movement_service(
    db: Session,
    movement_data: StockMovementCreate,
) -> StockMovement:
    source_stock_item = get_stock_item_by_product_and_location(
        db=db,
        product_id=movement_data.product_id,
        location_id=movement_data.from_location_id,
    )

    if source_stock_item is None:
        raise NotFoundError("Source stock item not found")

    destination_stock_item = get_stock_item_by_product_and_location(
        db=db,
        product_id=movement_data.product_id,
        location_id=movement_data.to_location_id,
    )

    if destination_stock_item is None:
        raise NotFoundError("Destination stock item not found")

    if source_stock_item.quantity < movement_data.quantity:
        raise StockInsufficientException("Not enough stock available")

    source_stock_item.quantity -= movement_data.quantity
    destination_stock_item.quantity += movement_data.quantity

    stock_movement = create_stock_movement(db, movement_data)

    db.commit()
    db.refresh(stock_movement)

    return stock_movement


def get_stock_movements_service(db: Session) -> list[StockMovement]:
    return get_stock_movements(db)
