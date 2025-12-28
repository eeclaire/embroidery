"""add pattern table

Revision ID: e6a2cfed5356
Revises:
Create Date: 2025-12-28 16:52:41.289505

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "e6a2cfed5356"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "patterns",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("source_id", sa.VARCHAR(), nullable=False),
        sa.Column("name", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("source_id"),
    )
    op.create_index("idx_name", "patterns", ["name"], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("idx_name", table_name="patterns")
    op.drop_table("patterns")
