from typing import List
from fastapi import APIRouter, Depends

from src.schemas.comment import CommentUpdateSchema, CommentSchema
from src.schemas.comment import CommentCreateSchema
from src.services.comment import CommentService, get_comment_service

router = APIRouter(
    prefix="/comment",
    tags=["comment"],
)

@router.get("/", response_model=List[CommentSchema])
async def get_all_comments(
        service: CommentService = Depends(get_comment_service),
):
    return await service.get_all()


@router.post("/")
async def create_comment(
        schema: CommentCreateSchema,
        service: CommentService = Depends(get_comment_service),
):
    return await service.create_one(schema)


@router.put("/{comment_id}", response_model=CommentUpdateSchema)
async def update_comment(
        comment_id: int,
        schema: CommentUpdateSchema,
        service: CommentService = Depends(get_comment_service),
):
    return await service.update_one(comment_id, schema)


@router.delete("/{comment_id}")
async def delete_comment(
        comment_id: int,
        service: CommentService = Depends(get_comment_service),
):
    return await service.delete(comment_id)


@router.get("/comments-daily-breakdown")
async def get_daily_breakdown(
        from_date: str,
        to_date: str,
        service: CommentService = Depends(get_comment_service),
):
    return await service.get_daily_breakdown(from_date, to_date)
