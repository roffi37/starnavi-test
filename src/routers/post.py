from fastapi import Depends
from fastapi.routing import APIRouter

from src.schemas.post import PostCreateSchema
from src.services.post import PostService, get_post_service

router = APIRouter(
    prefix="/post",
    tags=["posts"],
)


@router.get("/")
async def get_all_users(
        service: PostService = Depends(get_post_service)
):
    return await service.get_all()


@router.post("/")
async def create_post(
        schema: PostCreateSchema,
        service: PostService = Depends(get_post_service)
):
    return await service.create_one(schema)


@router.put("/{post_id}")
async def update_post(
        post_id: int,
        schema: PostCreateSchema,
        service: PostService = Depends(get_post_service)
):
    return await service.update_one(post_id, schema)


@router.delete("/{post_id}")
async def delete_post(
        post_id: int,
        service: PostService = Depends(get_post_service)
):
    return await service.delete(post_id)
