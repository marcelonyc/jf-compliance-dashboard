"""Add policies

Revision ID: aba90197c517
Revises: 81f81659d733
Create Date: 2024-11-27 16:07:31.210264

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
revision: str = "aba90197c517"
down_revision: Union[str, None] = "81f81659d733"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    if db_type == "sqlite":
        json_type = JSON
    else:
        json_type = JSONB

    op.create_table(
        "policies",
        sa.Column("name", sa.String, primary_key=True),
        sa.Column("type", sa.String),
        sa.Column("author", sa.String),
        sa.Column("rules", json_type),
        sa.Column("created", sa.String),
        sa.Column("modified", sa.String),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("project_key", sa.String, nullable=True),
    )


def downgrade() -> None:
    pass
