from typing import Annotated

from fastapi import Depends

from src.repositories.comment import get_comment_repository, CommentRepository
from src.services.base import BaseService
from src.utils.openai_moderator import check_for_swearing


class CommentService(BaseService):

    async def create_one(self, schema):
        data = schema.model_dump()
        data["is_blocked"] = check_for_swearing(data.get("content"))
        return await self.repository.create_one(data)


CommentRepositoryDependency = Annotated[CommentRepository, Depends(get_comment_repository)]

def get_comment_service(repository: CommentRepositoryDependency):
    return CommentService(repository)
