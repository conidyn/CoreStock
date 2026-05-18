from enum import StrEnum


class StockMovementType(StrEnum):
    PURCHASE = "purchase"
    SALE = "sale"
    TRANSFER = "transfer"
