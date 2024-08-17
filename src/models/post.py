from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import List

from src.schemas.post import PostSchema
from src.db.db import Base


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str]
    content: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    is_blocked: Mapped[bool] = mapped_column(default=False)
    author: Mapped["User"] = relationship(
        back_populates="posts"
    )
    comments: Mapped[List["Comment"]] = relationship(
        back_populates="post"
    )

    def to_read_model(self) -> PostSchema:
        return PostSchema(
            id=self.id,
            title=self.title,
            content=self.content,
            author_id=self.author_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_blocked=self.is_blocked,
        )
