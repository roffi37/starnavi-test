from fastapi import Depends
from fastapi.routing import APIRouter

from src.schemas.post import PostCreateSchema, PostUpdateSchema
from src.services.post import PostService, get_post_service
from src.utils.auth import get_current_user

router = APIRouter(
    prefix="/post",
    tags=["posts"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/")
async def get_all_posts(
        service: PostService = Depends(get_post_service),
):
    return await service.get_all()


@router.post("/", response_model=PostCreateSchema)
async def create_post(
        schema: PostCreateSchema,
        service: PostService = Depends(get_post_service),
):
    return await service.create_one(schema)


@router.put("/{post_id}", response_model=PostUpdateSchema)
async def update_post(
        post_id: int,
        schema: PostUpdateSchema,
        service: PostService = Depends(get_post_service),
):
    return await service.update_one(post_id, schema)


@router.delete("/{post_id}")
async def delete_post(
        post_id: int,
        service: PostService = Depends(get_post_service),
):
    return await service.delete(post_id)
