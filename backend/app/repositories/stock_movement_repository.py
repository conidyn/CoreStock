from sqlalchemy.orm import Session

from app.models.stock_item import StockItem
from app.models.stock_movement import StockMovement
from app.schemas.stock_movement import StockMovementCreate
from app.core.exceptions import NotFoundError, StockInsufficientException


def create_stock_movement(
    db: Session,
    movement_data: StockMovementCreate,
) -> StockMovement:
    source_stock_item = (
        db.query(StockItem)
        .filter(
            StockItem.product_id == movement_data.product_id,
            StockItem.location_id == movement_data.from_location_id,
        )
        .first()
    )

    destination_stock_item = (
        db.query(StockItem)
        .filter(
            StockItem.product_id == movement_data.product_id,
            StockItem.location_id == movement_data.to_location_id,
        )
        .first()
    )

    if source_stock_item is None:
        raise NotFoundError("Source stock item not found")

    if destination_stock_item is None:
        raise NotFoundError("Destination stock item not found")

    if source_stock_item.quantity < movement_data.quantity:
        raise StockInsufficientException("Not enough stock available")

    source_stock_item.quantity -= movement_data.quantity
    destination_stock_item.quantity += movement_data.quantity

    stock_movement = StockMovement(**movement_data.model_dump())

    db.add(stock_movement)

    db.commit()

    db.refresh(stock_movement)

    return stock_movement
