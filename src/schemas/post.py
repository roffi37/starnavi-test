from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PostCreateSchema(BaseModel):
    title: str
    content: str
    author_id: int


class PostSchema(PostCreateSchema):
    id: int
    is_blocked: bool
    created_at: datetime
    updated_at: Optional[datetime]
