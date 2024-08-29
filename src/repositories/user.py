from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.exceptions import relation_not_found
from src.exceptions import sign_in_error
from src.models.user import User
from src.config import Settings, get_settings
from src.db.db import get_async_session
from src.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    async def get_one_by_email(self, email: str) -> bytes:
        stmt = select(self.model).where(self.model.email == email)
        try:
            result = await self.session.execute(stmt)
            user = result.scalar()
            if user:
                return user.password
            raise sign_in_error
        except IntegrityError:
            raise relation_not_found

def get_user_repository(
        session: AsyncSession = Depends(get_async_session),
        settings: Settings = Depends(get_settings),
) -> UserRepository:
    return UserRepository(
        session=session,
        settings=settings,
        model=User,
    )
