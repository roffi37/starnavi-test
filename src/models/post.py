from sqlalchemy.orm import Mapped, relationship
from typing import List

from src.db.db import Base


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str]
    content: Mapped[str]
    authors: Mapped[List["User"]] = relationship(
        secondary="users_posts_associations",
        back_populates="posts",
        uselist=True,
    )
    comments: Mapped["Comment"]
