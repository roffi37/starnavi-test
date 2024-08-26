from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel


class CommentCreateSchema(BaseModel):
    content: str
    author_id: int
    parent_comment_id: Optional[int] = None
    post_id: int


class CommentUpdateSchema(BaseModel):
    blocked_at: Optional[datetime]
    likes: int
    dislikes: int



class CommentSchema(CommentUpdateSchema, CommentCreateSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]


class DailyBreakdown(BaseModel):
    date: date
    created_comments: int
    blocked_comments: int
