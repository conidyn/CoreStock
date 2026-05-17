from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.product import Product
from app.schemas.product import ProductCreate
from app.core.exceptions import ProductAlreadyExistsException


def create_product(db: Session, product_data: ProductCreate) -> Product:
    product = Product(**product_data.model_dump())

    db.add(product)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ProductAlreadyExistsException()

    db.refresh(product)

    return product


def get_products(db: Session) -> list[Product]:
    return db.query(Product).all()
