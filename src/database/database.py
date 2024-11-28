from sqlalchemy import (
    MetaData,
    create_engine,
    Boolean,
    Column,
    DateTime,
    Identity,
    Integer,
    MetaData,
    String,
    Table,
    Float,
    VARCHAR,
    CursorResult,
    Select,
    Insert,
    Update,
    Delete,
    func,
    LargeBinary,
)
from typing import Any

from sqlalchemy.ext.asyncio import create_async_engine
from config.app_config import get_settings
from .constants import DB_NAMING_CONVENTION
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.sqlite import JSON

# SQLModel
from sqlmodel import (
    Field,
    Session,
    SQLModel,
    create_engine as sqlmodel_create_engine,
)

DATABASE_URL = str(get_settings().db_url)
sync_db_url = DATABASE_URL.replace("+aiosqlite", "")
if "sqlite" in DATABASE_URL:
    engine = create_async_engine(
        DATABASE_URL,
        pool_pre_ping=True,
    )
    engine_sync = create_engine(sync_db_url)
    engine_sm_sync = sqlmodel_create_engine(sync_db_url, echo=True)
else:
    engine = create_async_engine(
        DATABASE_URL,
        pool_size=1,
        max_overflow=3,
        pool_pre_ping=True,
    )

    engine_sync = create_engine(
        sync_db_url,
        pool_size=1,
        max_overflow=3,
    )

    engine_sm_sync = sqlmodel_create_engine(
        sync_db_url,
        pool_size=1,
        max_overflow=3,
        echo=True,
    )

metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)


DATABASE_URL = str(get_settings().db_url)

json_type = None
sqlengine_type = None
if "sqlite" in DATABASE_URL:
    json_type = JSON
    sqlengine_type = "sqlite"
else:
    json_type = JSONB
    sqlengine_type = "postgresql"


class DashboardDB:
    def __init__(self, engine, engine_sync, engine_sm_sync) -> None:
        self.engine = engine
        self.engine_sync = engine_sync
        self.engine_sm_sync = engine_sm_sync

    async def fetch_one(
        self,
        select_query: Select,
    ) -> dict[str, Any] | None:
        async with self.engine.begin() as conn:
            cursor: CursorResult = await conn.execute(select_query)
            return cursor.first()._asdict() if cursor.rowcount > 0 else None

    async def fetch_all(
        self,
        select_query: Select,
    ) -> list[dict[str, Any]]:
        async with self.engine.begin() as conn:
            cursor: CursorResult = await conn.execute(select_query)
            return [r._asdict() for r in cursor.all()]

    def fetch_all_sync(
        self,
        select_query: Select,
    ) -> list[dict[str, Any]]:
        with self.engine_sync.begin() as conn:
            cursor: CursorResult = conn.execute(select_query)
            return [r._asdict() for r in cursor.all()]

    async def execute(self, select_query: Insert | Update | Delete) -> None:
        async with self.engine.begin() as conn:
            any_return = await conn.execute(select_query)
            return any_return

    def execute_sync(self, select_query: Insert | Update | Delete) -> None:
        with self.engine_sync.begin() as conn:
            any_return = conn.execute(select_query)
            return any_return

    def sm_add(self, obj: SQLModel) -> None:
        with Session(self.engine_sm_sync) as session:
            print(obj.model_dump)
            session.add(obj)
            session.commit()

    async def disconnect(self) -> None:
        await self.engine.dispose()


database = DashboardDB(engine, engine_sync, engine_sm_sync)
