from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class StockItem(Base):
    __tablename__ = "stock_items"

    __table_args__ = (
        UniqueConstraint(
            "product_id",
            "location_id",
            name="uq_stock_items_product_location",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
    )

    location_id: Mapped[int] = mapped_column(
        ForeignKey("stock_locations.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )
