from fastapi import Depends
from typing import Annotated

from src.schemas.post import PostCreateSchema
from src.repositories.post import PostRepository, get_post_repository
from src.services.base import BaseService
from src.utils.openai_moderator import check_for_swearing


class PostService(BaseService):

    async def create_one(self, schema: PostCreateSchema):
        data = schema.model_dump()
        data["is_blocked"] = check_for_swearing(data.get("content")) or check_for_swearing(data.get("title"))
        return await self.repository.create_one(data)

PostRepositoryDependency = Annotated[PostRepository, Depends(get_post_repository)]

def get_post_service(repository: PostRepositoryDependency):
    return PostService(repository)
