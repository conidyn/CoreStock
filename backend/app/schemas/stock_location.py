from typing import Literal

from pydantic import BaseModel, Field


class StockLocationCreate(BaseModel):
    name: str = Field(min_length=1)
    type: Literal["internal", "supplier", "customer"]


class StockLocationResponse(BaseModel):
    id: int
    name: str
    type: str

    model_config = {
        "from_attributes": True,
    }
