from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel


class PostCreateSchema(BaseModel):
    title: str
    content: str
    author_id: int
    is_auto_response: bool
    auto_response_delay: int


class PostUpdateSchema(PostCreateSchema):
    title: Optional[str] = None
    content: Optional[str] = None
    author_id: Optional[int] = None
    is_auto_response: Optional[bool] = None
    auto_response_delay: Optional[int] = None


class PostSchema(PostCreateSchema):
    id: int
    blocked_at: Optional[date]
    created_at: datetime
    updated_at: Optional[datetime]
