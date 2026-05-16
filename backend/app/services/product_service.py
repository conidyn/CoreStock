from sqlalchemy.orm import Session

from app.repositories.product_repository import create_product
from app.schemas.product import ProductCreate
from app.models.product import Product


def create_product_service(db: Session, product_data: ProductCreate) -> Product:
    return create_product(db, product_data)