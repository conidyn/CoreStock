from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.stock_item import StockItem
    from app.models.stock_movement import StockMovement


class StockLocation(Base):
    __tablename__ = "stock_locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    type: Mapped[str] = mapped_column(String, nullable=False)

    stock_items: Mapped[list["StockItem"]] = relationship(
        back_populates="location",
    )

    outgoing_movements: Mapped[list["StockMovement"]] = relationship(
        foreign_keys="StockMovement.from_location_id",
        back_populates="from_location",
    )

    incoming_movements: Mapped[list["StockMovement"]] = relationship(
        foreign_keys="StockMovement.to_location_id",
        back_populates="to_location",
    )
