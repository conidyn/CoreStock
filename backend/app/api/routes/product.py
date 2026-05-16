from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import create_product_service
from app.core.exceptions import ProductAlreadyExistsException

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("", response_model=ProductResponse)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    try:
        return create_product_service(db, product_data)

    except ProductAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product SKU already exists",
        )
