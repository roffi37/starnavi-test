from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from src.schemas.comment import CommentSchema
from src.schemas.user import UserSchema


class PostCreateSchema(BaseModel):
    id: int
    title: str
    content: str
    authors: List[UserSchema]
    comments: List[CommentSchema]



class PostSchema(PostCreateSchema):
    created_at: datetime
    updated_at: Optional[datetime]
