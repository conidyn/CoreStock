from pydantic import BaseModel, Field


class StockItemCreate(BaseModel):
    product_id: int = Field(gt=0)
    location_id: int = Field(gt=0)
    quantity: int = Field(ge=0)


class StockItemResponse(BaseModel):
    id: int
    product_id: int
    location_id: int
    quantity: int

    model_config = {
        "from_attributes": True,
    }
