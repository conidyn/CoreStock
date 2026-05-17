from __future__ import annotations

from typing import TYPE_CHECKING

from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.stock_location import StockLocation


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
    )

    from_location_id: Mapped[int] = mapped_column(
        ForeignKey("stock_locations.id"),
        nullable=False,
    )

    to_location_id: Mapped[int] = mapped_column(
        ForeignKey("stock_locations.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    movement_type: Mapped[str] = mapped_column(String, nullable=False)

    reason: Mapped[str] = mapped_column(String, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC),
    )

    product: Mapped["Product"] = relationship(
        back_populates="stock_movements",
    )

    from_location: Mapped["StockLocation"] = relationship(
        foreign_keys=[from_location_id],
        back_populates="outgoing_movements",
    )

    to_location: Mapped["StockLocation"] = relationship(
        foreign_keys=[to_location_id],
        back_populates="incoming_movements",
    )
