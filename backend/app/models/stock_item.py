from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.stock_location import StockLocation


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

    product: Mapped["Product"] = relationship(
        back_populates="stock_items",
    )

    location: Mapped["StockLocation"] = relationship(
        back_populates="stock_items",
    )
