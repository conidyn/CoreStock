from sqlalchemy.orm import Session

from app.repositories.product_repository import create_product, get_products
from app.repositories.stock_movement_repository import (
    get_stock_movements_by_product_id,
)
from app.schemas.product import ProductCreate
from app.models.product import Product
from app.models.stock_movement import StockMovement


def create_product_service(db: Session, product_data: ProductCreate) -> Product:
    return create_product(db, product_data)


def get_products_service(db: Session) -> list[Product]:
    return get_products(db)


def get_product_movements_service(
    db: Session,
    product_id: int,
) -> list[StockMovement]:
    return get_stock_movements_by_product_id(db, product_id)
