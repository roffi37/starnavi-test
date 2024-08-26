from datetime import date, timedelta
from typing import List

from fastapi import APIRouter, Depends, Query, BackgroundTasks

from src.schemas.comment import CommentUpdateSchema, CommentSchema
from src.schemas.comment import CommentCreateSchema
from src.services.comment import CommentService, get_comment_service
from src.utils.auth import get_current_user


router = APIRouter(
    prefix="/comment",
    tags=["comment"],
    dependencies=[Depends(get_current_user)]
)


@router.get("/", response_model=List[CommentSchema])
async def get_all_comments(
        service: CommentService = Depends(get_comment_service),
):
    return await service.get_all()


@router.post("/")
async def create_comment(
        schema: CommentCreateSchema,
        background_task: BackgroundTasks,
        service: CommentService = Depends(get_comment_service),
):
    return await service.create_one(schema, background_task)


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
        from_date: str = Query(default=date.today() - timedelta(days=30)),
        to_date: str = Query(default=date.today()),
        service: CommentService = Depends(get_comment_service),
):
    return await service.get_daily_breakdown(from_date, to_date)
