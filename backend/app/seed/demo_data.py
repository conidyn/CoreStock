from sqlalchemy.orm import Session

from app.models.enums import (
    StockLocationType,
    StockMovementType,
)
from app.models.product import Product
from app.models.stock_item import StockItem
from app.models.stock_location import StockLocation
from app.models.stock_movement import StockMovement


def seed_demo_data(db: Session) -> None:
    if db.query(Product).filter(Product.sku == "DELL-5450").first():
        print("Demo data already exists.")
        return

    supplier = StockLocation(
        name="TechSupplier Europe",
        type=StockLocationType.SUPPLIER,
    )

    warehouse_liege = StockLocation(
        name="Liège Main Warehouse",
        type=StockLocationType.INTERNAL,
    )

    warehouse_brussels = StockLocation(
        name="Brussels Secondary Warehouse",
        type=StockLocationType.INTERNAL,
    )

    customer = StockLocation(
        name="Demo Customer",
        type=StockLocationType.CUSTOMER,
    )

    db.add_all(
        [
            supplier,
            warehouse_liege,
            warehouse_brussels,
            customer,
        ]
    )

    laptop = Product(
        name="Dell Latitude 5450",
        sku="DELL-5450",
        category="Laptops",
        unit="pcs",
        min_stock_threshold=5,
    )

    keyboard = Product(
        name="Logitech MX Keys",
        sku="LOGI-MXKEYS",
        category="Accessories",
        unit="pcs",
        min_stock_threshold=10,
    )

    label_printer = Product(
        name="Zebra Label Printer",
        sku="ZEBRA-ZD421",
        category="Printers",
        unit="pcs",
        min_stock_threshold=2,
    )

    db.add_all(
        [
            laptop,
            keyboard,
            label_printer,
        ]
    )

    db.flush()

    stock_items = [
        StockItem(
            product_id=laptop.id,
            location_id=warehouse_liege.id,
            quantity=3,
        ),
        StockItem(
            product_id=keyboard.id,
            location_id=warehouse_liege.id,
            quantity=18,
        ),
        StockItem(
            product_id=keyboard.id,
            location_id=warehouse_brussels.id,
            quantity=5,
        ),
        StockItem(
            product_id=label_printer.id,
            location_id=warehouse_brussels.id,
            quantity=1,
        ),
    ]

    db.add_all(stock_items)

    movements = [
        StockMovement(
            product_id=laptop.id,
            from_location_id=supplier.id,
            to_location_id=warehouse_liege.id,
            quantity=10,
            movement_type=StockMovementType.PURCHASE,
            reason="Supplier delivery to Liège warehouse",
        ),
        StockMovement(
            product_id=laptop.id,
            from_location_id=warehouse_liege.id,
            to_location_id=customer.id,
            quantity=7,
            movement_type=StockMovementType.SALE,
            reason="Customer laptop shipment",
        ),
        StockMovement(
            product_id=keyboard.id,
            from_location_id=supplier.id,
            to_location_id=warehouse_liege.id,
            quantity=23,
            movement_type=StockMovementType.PURCHASE,
            reason="Supplier keyboard delivery",
        ),
        StockMovement(
            product_id=keyboard.id,
            from_location_id=warehouse_liege.id,
            to_location_id=warehouse_brussels.id,
            quantity=5,
            movement_type=StockMovementType.TRANSFER,
            reason="Warehouse redistribution to Brussels",
        ),
        StockMovement(
            product_id=label_printer.id,
            from_location_id=supplier.id,
            to_location_id=warehouse_brussels.id,
            quantity=2,
            movement_type=StockMovementType.PURCHASE,
            reason="Supplier printer delivery",
        ),
        StockMovement(
            product_id=label_printer.id,
            from_location_id=warehouse_brussels.id,
            to_location_id=customer.id,
            quantity=1,
            movement_type=StockMovementType.SALE,
            reason="Customer printer shipment",
        ),
    ]

    db.add_all(movements)

    db.commit()

    print("Demo data seeded successfully.")
