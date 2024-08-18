from datetime import date

from fastapi import Depends
from numpy.ma.core import resize
from pydantic_settings import BaseSettings
from sqlalchemy import select, func, case, between, union_all, Integer, text
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.comment import DailyBreakdown
from src.config import get_settings
from src.db.db import get_async_session
from src.models.comment import Comment
from src.repositories.base import BaseRepository


class CommentRepository(BaseRepository):

    async def get_daily_breakdown(self, from_date, to_date):
        stmt = (
            select(
                func.date(self.model.created_at),
                func.count(self.model.id),
                func.count(func.nullif(self.model.blocked_at, None))
            )
            .where(self.model.created_at.between(from_date, to_date))
            .group_by(func.date(self.model.created_at))
            .order_by(func.date(self.model.created_at))
        )

        result = await self.session.execute(stmt)

        daily_breakdown = [
            DailyBreakdown(
                date=row[0],
                created_comments=row[1],
                blocked_comments=row[2],
            ) for row in result.all()
        ]

        return daily_breakdown


def get_comment_repository(
        session: AsyncSession = Depends(get_async_session),
        settings: BaseSettings = Depends(get_settings),
):
    return CommentRepository(
        session=session,
        settings=settings,
        model=Comment,
    )
