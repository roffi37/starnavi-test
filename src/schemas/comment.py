from datetime import datetime
from pydantic import BaseModel

from src.schemas.user import UserSchema


class CommentSchema(BaseModel):
    id: int
    content: str
    author: UserSchema
    likes: int
    dislikes: int
    created_at: datetime
