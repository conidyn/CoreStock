"""add stock movement type enum

Revision ID: ed760b4d7bfb
Revises: f4c33a8cbefd
Create Date: 2026-05-18 16:22:07.025735

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "ed760b4d7bfb"
down_revision: Union[str, Sequence[str], None] = "f4c33a8cbefd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


stock_movement_type = sa.Enum(
    "purchase",
    "sale",
    "transfer",
    name="stock_movement_type",
)


def upgrade() -> None:
    stock_movement_type.create(op.get_bind(), checkfirst=True)

    op.execute("""
        ALTER TABLE stock_movements
        ALTER COLUMN movement_type
        TYPE stock_movement_type
        USING movement_type::stock_movement_type
        """)


def downgrade() -> None:
    op.execute("""
        ALTER TABLE stock_movements
        ALTER COLUMN movement_type
        TYPE VARCHAR
        USING movement_type::text
        """)

    stock_movement_type.drop(op.get_bind(), checkfirst=True)
