from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import List

from src.db.db import Base


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str]
    content: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(
        "User",
        back_populates="posts"
    )
    comments: Mapped[List["Comment"]] = relationship(
        "Comment",
        back_populates="post"
    )
