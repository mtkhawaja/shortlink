"""create shortlink table

Revision ID: 707f3705117b
Revises: 91979b40eb38
Create Date: 2021-03-28 03:11:44.112500-04:00

"""
from alembic import op
import sqlalchemy as sa
from datetime import timedelta
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = "707f3705117b"
down_revision = "91979b40eb38"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "shortlink",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("original_url", sa.String, nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime,
            server_default=func.now(),
            nullable=False,
        ),
        sa.Column(
            "time_to_live",
            sa.Interval,
            default=timedelta(days=1),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table("shortlink")
