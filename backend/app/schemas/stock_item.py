from pydantic import BaseModel, Field


class StockItemCreate(BaseModel):
    product_id: int = Field(gt=0)
    location_id: int = Field(gt=0)
    quantity: int = Field(ge=0)


class StockItemProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    min_stock_threshold: int

    model_config = {
        "from_attributes": True,
    }


class StockItemLocationResponse(BaseModel):
    id: int
    name: str
    type: str

    model_config = {
        "from_attributes": True,
    }


class StockItemResponse(BaseModel):
    id: int
    product_id: int
    location_id: int
    quantity: int

    model_config = {
        "from_attributes": True,
    }


class StockItemDetailResponse(BaseModel):
    id: int
    quantity: int
    product: StockItemProductResponse
    location: StockItemLocationResponse

    model_config = {
        "from_attributes": True,
    }
