from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.stats import DashboardStatsResponse
from app.services.stats_service import get_dashboard_stats_service

router = APIRouter(
    prefix="/stats",
    tags=["Stats"],
)


@router.get(
    "/dashboard",
    response_model=DashboardStatsResponse,
)
def get_dashboard_stats(
    db: Session = Depends(get_db),
):
    return get_dashboard_stats_service(db)
