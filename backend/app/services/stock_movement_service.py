from sqlalchemy.orm import Session

from app.core.exceptions import (
    InvalidLocationTransferException,
    NotFoundError,
    StockInsufficientException,
)
from app.models.enums import StockLocationType, StockMovementType
from app.models.stock_location import StockLocation
from app.models.stock_movement import StockMovement
from app.repositories.stock_location_repository import get_stock_location_by_id
from app.repositories.stock_movement_repository import (
    create_stock_movement,
    get_stock_item_by_product_and_location,
    get_stock_movements,
)
from app.schemas.stock_movement import StockMovementCreate


def validate_movement_locations(
    movement_type: StockMovementType,
    from_location: StockLocation,
    to_location: StockLocation,
) -> None:
    valid_transfers = {
        StockMovementType.PURCHASE: (
            StockLocationType.SUPPLIER,
            StockLocationType.INTERNAL,
        ),
        StockMovementType.SALE: (
            StockLocationType.INTERNAL,
            StockLocationType.CUSTOMER,
        ),
        StockMovementType.TRANSFER: (
            StockLocationType.INTERNAL,
            StockLocationType.INTERNAL,
        ),
    }

    expected_from_type, expected_to_type = valid_transfers[movement_type]

    if from_location.type != expected_from_type or to_location.type != expected_to_type:
        raise InvalidLocationTransferException(
            f"Invalid location transfer for movement type '{movement_type}'"
        )


def create_stock_movement_service(
    db: Session,
    movement_data: StockMovementCreate,
) -> StockMovement:
    from_location = get_stock_location_by_id(
        db=db,
        location_id=movement_data.from_location_id,
    )

    if from_location is None:
        raise NotFoundError("Source location not found")

    to_location = get_stock_location_by_id(
        db=db,
        location_id=movement_data.to_location_id,
    )

    if to_location is None:
        raise NotFoundError("Destination location not found")

    validate_movement_locations(
        movement_type=movement_data.movement_type,
        from_location=from_location,
        to_location=to_location,
    )

    source_stock_item = get_stock_item_by_product_and_location(
        db=db,
        product_id=movement_data.product_id,
        location_id=movement_data.from_location_id,
    )

    if source_stock_item is None:
        raise NotFoundError("Source stock item not found")

    destination_stock_item = get_stock_item_by_product_and_location(
        db=db,
        product_id=movement_data.product_id,
        location_id=movement_data.to_location_id,
    )

    if destination_stock_item is None:
        raise NotFoundError("Destination stock item not found")

    if source_stock_item.quantity < movement_data.quantity:
        raise StockInsufficientException("Not enough stock available")

    source_stock_item.quantity -= movement_data.quantity
    destination_stock_item.quantity += movement_data.quantity

    stock_movement = create_stock_movement(db, movement_data)

    db.commit()
    db.refresh(stock_movement)

    return stock_movement


def get_stock_movements_service(db: Session) -> list[StockMovement]:
    return get_stock_movements(db)
