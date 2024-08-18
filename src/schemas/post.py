from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel


class PostCreateSchema(BaseModel):
    title: str
    content: str
    author_id: int


class PostSchema(PostCreateSchema):
    id: int
    blocked_at: Optional[date]
    created_at: datetime
    updated_at: Optional[datetime]
