from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.product import router as product_router
from app.api.routes.stock_location import router as stock_location_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(product_router)
api_router.include_router(stock_location_router)
