from datetime import datetime
from typing import AsyncGenerator

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config import get_settings

settings = get_settings()

engine = create_async_engine(settings.database.generate_async_database_url())
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now(), nullable=True)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
