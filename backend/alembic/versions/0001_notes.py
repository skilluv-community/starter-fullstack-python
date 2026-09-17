"""notes table

Revision ID: 0001
Revises:
Create Date: 2026-07-22

"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "notes",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("text", sa.String(500), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("notes_created_at_idx", "notes", ["created_at"])


def downgrade() -> None:
    op.drop_index("notes_created_at_idx", table_name="notes")
    op.drop_table("notes")
