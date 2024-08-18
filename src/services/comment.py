from datetime import datetime, UTC
from fastapi import Depends

from src.repositories.comment import get_comment_repository, CommentRepository
from src.services.base import BaseService
from src.utils.openai_moderator import check_for_swearing


class CommentService(BaseService):

    async def create_one(self, schema):
        data = schema.model_dump()
        if check_for_swearing(data.get("content")):
            data["blocked_at"] = datetime.now(UTC)
        return await self.repository.create_one(data)

    async def get_daily_breakdown(self, from_date: str, to_date: str):
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        to_date = datetime.strptime(to_date, "%Y-%m-%d").replace(hour=23, minute=59, second=59)
        return await self.repository.get_daily_breakdown(from_date, to_date)


def get_comment_service(repository: CommentRepository = Depends(get_comment_repository)):
    return CommentService(repository)
