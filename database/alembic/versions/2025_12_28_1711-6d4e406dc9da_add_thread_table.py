"""add thread table

Revision ID: 6d4e406dc9da
Revises: e6a2cfed5356
Create Date: 2025-12-28 17:11:56.215056

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "6d4e406dc9da"
down_revision: Union[str, Sequence[str], None] = "e6a2cfed5356"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "threads",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            primary_key=True,
            nullable=False,
        ),
        sa.Column("color_code", sa.VARCHAR(length=8), unique=True, nullable=False),
        sa.Column("color_desc", sa.VARCHAR(length=32), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("threads")
