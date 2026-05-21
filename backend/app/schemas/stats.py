from pydantic import BaseModel


class MovementBreakdownResponse(BaseModel):
    purchase: int = 0
    transfer: int = 0
    sale: int = 0


class DashboardStatsResponse(BaseModel):
    total_products: int
    total_stock_quantity: int
    low_stock_count: int
    total_movements: int
    movement_breakdown: MovementBreakdownResponse
