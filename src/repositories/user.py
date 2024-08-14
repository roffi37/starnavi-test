from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.user import User
from src.config import Settings, get_settings
from src.db.db import get_async_session
from src.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    model = User

    async def get_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]

    async def get_one(self, id_):
        pass

    async def create_one(self, data):
        stmt = insert(self.model).values(data).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar().to_read_model()

    async def update_one(self, id_, data):
        pass

    async def delete_one(self, id_):
        pass


def get_user_repository(
        session: AsyncSession = Depends(get_async_session),
        settings: Settings = Depends(get_settings),
) -> UserRepository:
    return UserRepository(
        session=session,
        settings=settings,
    )
