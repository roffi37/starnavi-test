from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import get_settings, Settings
from src.db.db import get_async_session
from src.models.post import Post
from src.repositories.base import BaseRepository


class PostRepository(BaseRepository):
    pass


def get_post_repository(
        session: AsyncSession = Depends(get_async_session),
        settings: Settings = Depends(get_settings),
):
    return PostRepository(
        session=session,
        settings=settings,
        model=Post,
    )