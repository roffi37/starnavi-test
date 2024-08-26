from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import List

from src.schemas.post import PostSchema
from src.db.db import Base


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str]
    content: Mapped[str]
    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL")
    )
    blocked_at: Mapped[date] = mapped_column(nullable=True)
    is_auto_response: Mapped[bool] = mapped_column(default=False)
    auto_response_delay: Mapped[int] = mapped_column(default=5)
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
            is_auto_response=self.is_auto_response,
            auto_response_delay=self.auto_response_delay,
            created_at=self.created_at,
            updated_at=self.updated_at,
            blocked_at=self.blocked_at,
        )
