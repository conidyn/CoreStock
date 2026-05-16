from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=1)
    sku: str = Field(min_length=1)
    category: str = Field(min_length=1)
    unit: str = Field(min_length=1)
    min_stock_threshold: int = Field(default=0, ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    category: str
    unit: str
    min_stock_threshold: int

    model_config = {
        "from_attributes": True,
    }