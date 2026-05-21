from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.stock_item import StockItem
from app.models.stock_movement import StockMovement


def get_total_products(db: Session) -> int:
    return db.query(func.count(Product.id)).scalar() or 0


def get_total_stock_quantity(db: Session) -> int:
    return db.query(func.coalesce(func.sum(StockItem.quantity), 0)).scalar() or 0


def get_low_stock_count(db: Session) -> int:
    return (
        db.query(func.count(StockItem.id))
        .join(Product)
        .filter(StockItem.quantity <= Product.min_stock_threshold)
        .scalar()
        or 0
    )


def get_total_movements(db: Session) -> int:
    return db.query(func.count(StockMovement.id)).scalar() or 0


def get_movement_breakdown(db: Session) -> dict[str, int]:
    rows = (
        db.query(
            StockMovement.movement_type,
            func.count(StockMovement.id),
        )
        .group_by(StockMovement.movement_type)
        .all()
    )

    return {movement_type.value: count for movement_type, count in rows}
