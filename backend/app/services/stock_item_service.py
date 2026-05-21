from sqlalchemy.orm import Session

from app.models.stock_item import StockItem
from app.repositories.stock_item_repository import (
    create_stock_item,
    get_low_stock_items,
    get_stock_items,
)
from app.schemas.stock_item import StockItemCreate


def create_stock_item_service(
    db: Session,
    stock_item_data: StockItemCreate,
) -> StockItem:
    return create_stock_item(db, stock_item_data)


def get_stock_items_service(
    db: Session,
) -> list[StockItem]:
    return get_stock_items(db)


def get_low_stock_items_service(
    db: Session,
) -> list[StockItem]:
    return get_low_stock_items(db)
