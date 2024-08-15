from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.user import User
from src.config import Settings, get_settings
from src.db.db import get_async_session
from src.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    pass


def get_user_repository(
        session: AsyncSession = Depends(get_async_session),
        settings: Settings = Depends(get_settings),
) -> UserRepository:
    return UserRepository(
        session=session,
        settings=settings,
        model=User,
    )
