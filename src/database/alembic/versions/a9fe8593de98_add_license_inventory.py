"""Add license inventory

Revision ID: a9fe8593de98
Revises: aba90197c517
Create Date: 2024-12-06 10:09:11.480183

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.sqlite import JSON
import os

os.environ["RUN_MODE"] = "alembic"
from src.config.app_config import get_settings

app_config = get_settings()
db_type = "postgresql"
if "sqlite" in app_config.db_url:
    db_type = "sqlite"

# revision identifiers, used by Alembic.
revision: str = "a9fe8593de98"
down_revision: Union[str, None] = "aba90197c517"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "repo_updated_hwm_table",
        sa.Column(
            "updated_hwm", sa.DateTime, nullable=False, primary_key=True
        ),
    )

    op.create_table(
        "licenseresult",
        sa.Column("uri", sa.String, primary_key=True),
        sa.Column("license", sa.String, primary_key=True),
        sa.Column("repo", sa.String, primary_key=True),
        sa.Column("found", sa.String),
        sa.Column("status", sa.String),
    )


def downgrade() -> None:
    pass
