from sqlalchemy.orm import Session

from app.models.stock_item import StockItem
from app.models.stock_movement import StockMovement
from app.schemas.stock_movement import StockMovementCreate


def get_stock_item_by_product_and_location(
    db: Session,
    product_id: int,
    location_id: int,
) -> StockItem | None:
    return (
        db.query(StockItem)
        .filter(
            StockItem.product_id == product_id,
            StockItem.location_id == location_id,
        )
        .first()
    )


def create_stock_movement(
    db: Session,
    movement_data: StockMovementCreate,
) -> StockMovement:
    stock_movement = StockMovement(**movement_data.model_dump())

    db.add(stock_movement)
    db.flush()
    db.refresh(stock_movement)

    return stock_movement


def get_stock_movements(db: Session) -> list[StockMovement]:
    return db.query(StockMovement).order_by(StockMovement.created_at.desc()).all()
