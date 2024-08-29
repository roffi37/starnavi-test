from datetime import datetime, UTC
from fastapi import Depends
from fastapi.background import BackgroundTasks

from src.schemas.comment import CommentSchema
from src.repositories.comment import get_comment_repository, CommentRepository
from src.services.base import BaseService
from src.utils.openai_moderator import check_for_swearing
from src.utils.autoreply import create_auto_reply


class CommentService(BaseService):

    async def _create_auto_reply_comment(self, created_comment: CommentSchema):
        related_post = await self.repository.check_if_related_to_post_with_auto_response(created_comment.post_id)
        if related_post.is_auto_response and created_comment.author_id != related_post.author_id:
            data = await create_auto_reply(created_comment, related_post)
            return await self.repository.create_one(data.model_dump())

    async def create_one(self, schema, background_tasks: BackgroundTasks = Depends(BackgroundTasks)):
        data = schema.model_dump()
        if check_for_swearing(data.get("content")):
            data["blocked_at"] = datetime.now(UTC)
        created_comment = await self.repository.create_one(data)
        background_tasks.add_task(self._create_auto_reply_comment, created_comment)
        return created_comment

    async def get_daily_breakdown(self, from_date: str, to_date: str):
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        to_date = datetime.strptime(to_date, "%Y-%m-%d").replace(hour=23, minute=59, second=59)
        return await self.repository.get_daily_breakdown(from_date, to_date)


def get_comment_service(repository: CommentRepository = Depends(get_comment_repository)):
    return CommentService(repository)
