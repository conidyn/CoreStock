from datetime import datetime
from app.models.enums import StockMovementType

from pydantic import BaseModel, Field, field_validator


class StockMovementCreate(BaseModel):
    product_id: int = Field(gt=0)
    from_location_id: int = Field(gt=0)
    to_location_id: int = Field(gt=0)
    quantity: int = Field(gt=0)
    movement_type: StockMovementType
    reason: str = Field(min_length=3, max_length=160)

    @field_validator("reason")
    @classmethod
    def clean_reason(cls, value: str) -> str:
        cleaned_value = value.strip()

        if not cleaned_value:
            raise ValueError("Reason is required")

        return cleaned_value


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
