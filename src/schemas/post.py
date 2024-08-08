from datetime import datetime
from typing import List
from pydantic import BaseModel

from src.schemas.comment import CommentSchema
from src.schemas.user import UserSchema


class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    authors: List[UserSchema]
    comments: List[CommentSchema]
    created_at: datetime
