from datetime import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    content: str
    author: "User"
    likes: int
    dislikes: int
    created_at: datetime
