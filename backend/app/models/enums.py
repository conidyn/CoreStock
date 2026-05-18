from enum import StrEnum


class StockMovementType(StrEnum):
    PURCHASE = "purchase"
    SALE = "sale"
    TRANSFER = "transfer"


class StockLocationType(StrEnum):
    INTERNAL = "internal"
    SUPPLIER = "supplier"
    CUSTOMER = "customer"
