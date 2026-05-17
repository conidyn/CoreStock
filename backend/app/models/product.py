from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, nullable=False)

    sku: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )

    category: Mapped[str] = mapped_column(String, nullable=False)

    unit: Mapped[str] = mapped_column(String, nullable=False)

    min_stock_threshold: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    stock_items: Mapped[list["StockItem"]] = relationship(
        back_populates="product",
    )

    stock_movements: Mapped[list["StockMovement"]] = relationship(
        back_populates="product",
    )
