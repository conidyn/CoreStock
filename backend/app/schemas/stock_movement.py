from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class StockMovementCreate(BaseModel):
    product_id: int = Field(gt=0)
    from_location_id: int = Field(gt=0)
    to_location_id: int = Field(gt=0)
    quantity: int = Field(gt=0)
    movement_type: Literal["purchase", "sale", "transfer"]
    reason: str = Field(min_length=1)


class StockMovementResponse(BaseModel):
    id: int
    product_id: int
    from_location_id: int
    to_location_id: int
    quantity: int
    movement_type: str
    reason: str
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }
