"""add stock location type enum

Revision ID: 50f773cc709c
Revises: ed760b4d7bfb
Create Date: 2026-05-18 22:23:54.672077

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "50f773cc709c"
down_revision: Union[str, Sequence[str], None] = "ed760b4d7bfb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


stock_location_type = sa.Enum(
    "internal",
    "supplier",
    "customer",
    name="stock_location_type",
)


def upgrade() -> None:
    stock_location_type.create(op.get_bind(), checkfirst=True)

    op.execute("""
        ALTER TABLE stock_locations
        ALTER COLUMN type
        TYPE stock_location_type
        USING type::stock_location_type
        """)


def downgrade() -> None:
    op.execute("""
        ALTER TABLE stock_locations
        ALTER COLUMN type
        TYPE VARCHAR
        USING type::text
        """)

    stock_location_type.drop(op.get_bind(), checkfirst=True)
