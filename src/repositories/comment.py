from fastapi import Depends
from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import get_settings
from src.db.db import get_async_session
from src.models.comment import Comment
from src.repositories.base import BaseRepository


class CommentRepository(BaseRepository):
    pass


def get_comment_repository(
        session: AsyncSession = Depends(get_async_session),
        settings: BaseSettings = Depends(get_settings),
):
    return CommentRepository(
        session=session,
        settings=settings,
        model=Comment,
    )
