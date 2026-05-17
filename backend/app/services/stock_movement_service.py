from sqlalchemy.orm import Session

from app.models.stock_movement import StockMovement
from app.repositories.stock_movement_repository import create_stock_movement
from app.schemas.stock_movement import StockMovementCreate


def create_stock_movement_service(
    db: Session,
    movement_data: StockMovementCreate,
) -> StockMovement:
    return create_stock_movement(db, movement_data)
