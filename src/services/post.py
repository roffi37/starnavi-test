from datetime import UTC, datetime

from fastapi import Depends

from src.schemas.post import PostCreateSchema
from src.repositories.post import PostRepository, get_post_repository
from src.services.base import BaseService
from src.utils.openai_moderator import check_for_swearing


class PostService(BaseService):

    async def create_one(self, schema: PostCreateSchema):
        data = schema.model_dump()
        if check_for_swearing(data.get("content")) or check_for_swearing(data.get("title")):
            data["blocked_at"] = datetime.now(UTC)
        return await self.repository.create_one(data)

    async def update_one(self, id_, schema):
        data = schema.model_dump()
        return await self.repository.update_one(id_, data)

def get_post_service(repository: PostRepository = Depends(get_post_repository)):
    return PostService(repository)
