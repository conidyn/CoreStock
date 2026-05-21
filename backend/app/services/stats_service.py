from sqlalchemy.orm import Session

from app.repositories.stats_repository import (
    get_low_stock_count,
    get_movement_breakdown,
    get_total_movements,
    get_total_products,
    get_total_stock_quantity,
)
from app.schemas.stats import DashboardStatsResponse, MovementBreakdownResponse


def get_dashboard_stats_service(db: Session) -> DashboardStatsResponse:
    movement_breakdown = get_movement_breakdown(db)

    return DashboardStatsResponse(
        total_products=get_total_products(db),
        total_stock_quantity=get_total_stock_quantity(db),
        low_stock_count=get_low_stock_count(db),
        total_movements=get_total_movements(db),
        movement_breakdown=MovementBreakdownResponse(
            purchase=movement_breakdown.get("purchase", 0),
            transfer=movement_breakdown.get("transfer", 0),
            sale=movement_breakdown.get("sale", 0),
        ),
    )
