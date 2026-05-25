from datetime import datetime
from app.models.enums import StockMovementType

from pydantic import BaseModel, Field


class StockMovementCreate(BaseModel):
    product_id: int = Field(gt=0)
    from_location_id: int = Field(gt=0)
    to_location_id: int = Field(gt=0)
    quantity: int = Field(gt=0)
    movement_type: StockMovementType
    reason: str = Field(min_length=1)


class StockMovementProductResponse(BaseModel):
    id: int
    name: str
    sku: str

    model_config = {
        "from_attributes": True,
    }


class StockMovementLocationResponse(BaseModel):
    id: int
    name: str
    type: str

    model_config = {
        "from_attributes": True,
    }


class StockMovementResponse(BaseModel):
    id: int
    product_id: int
    from_location_id: int
    to_location_id: int
    quantity: int
    movement_type: StockMovementType
    reason: str
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }


class StockMovementDetailResponse(BaseModel):
    id: int
    quantity: int
    movement_type: StockMovementType
    reason: str
    created_at: datetime
    product: StockMovementProductResponse
    from_location: StockMovementLocationResponse
    to_location: StockMovementLocationResponse

    model_config = {
        "from_attributes": True,
    }
