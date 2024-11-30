from __future__ import annotations

from typing import List, Optional, Annotated
from datetime import date, datetime
from database.database import json_type
from pydantic import BaseModel, types as pydantic_types

from sqlmodel import Field, SQLModel, ARRAY


class Violations(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str
    severity: str
    type: str
    infected_components: list = Field(sa_type=json_type)
    created: datetime
    watch_name: str
    issue_id: str
    violation_details_url: str
    impacted_artifacts: list = Field(sa_type=json_type)


class Model(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    total_violations: int
    violations: list = Field(sa_type=json_type)


class Violations_Hwm_Table(SQLModel, table=True):
    __tablename__ = "violations_hwm"
    created_hwm: datetime | None = Field(default=None, primary_key=True)
