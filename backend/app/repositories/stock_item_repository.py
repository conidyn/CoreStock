from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError

from app.models.stock_item import StockItem
from app.schemas.stock_item import StockItemCreate
from app.core.exceptions import ConflictError
from app.models.product import Product


def create_stock_item(
    db: Session,
    stock_item_data: StockItemCreate,
) -> StockItem:

    stock_item = StockItem(**stock_item_data.model_dump())

    db.add(stock_item)

    try:
        db.commit()

    except IntegrityError:
        db.rollback()

        raise ConflictError("Stock item already exists for this product and location")

    db.refresh(stock_item)

    return stock_item


def get_stock_items(db: Session) -> list[StockItem]:
    return (
        db.query(StockItem)
        .options(
            joinedload(StockItem.product),
            joinedload(StockItem.location),
        )
        .all()
    )


def get_low_stock_items(db: Session) -> list[StockItem]:
    return (
        db.query(StockItem)
        .join(Product)
        .options(
            joinedload(StockItem.product),
            joinedload(StockItem.location),
        )
        .filter(StockItem.quantity <= Product.min_stock_threshold)
        .all()
    )
