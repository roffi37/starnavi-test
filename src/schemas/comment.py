from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CommentCreateSchema(BaseModel):
    content: str
    author_id: int
    post_id: int


class CommentUpdateSchema(BaseModel):
    is_blocked: bool
    likes: int
    dislikes: int



class CommentSchema(CommentUpdateSchema, CommentCreateSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
