from datetime import datetime
from typing import List

from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    authors: List["User"]
    tags: List["Tag"]
    created_at: datetime
