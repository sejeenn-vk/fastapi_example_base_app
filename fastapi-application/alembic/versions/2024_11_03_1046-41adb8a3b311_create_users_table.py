"""create users table

Revision ID: 41adb8a3b311
Revises: 
Create Date: 2024-11-03 10:46:57.693267

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "41adb8a3b311"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )


def downgrade() -> None:
    op.drop_table("users")
