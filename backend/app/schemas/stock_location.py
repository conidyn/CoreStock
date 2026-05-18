from app.models.enums import StockLocationType

from pydantic import BaseModel, Field


class StockLocationCreate(BaseModel):
    name: str = Field(min_length=1)
    type: StockLocationType


class StockLocationResponse(BaseModel):
    id: int
    name: str
    type: StockLocationType

    model_config = {
        "from_attributes": True,
    }
