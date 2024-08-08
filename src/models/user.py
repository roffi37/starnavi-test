from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from uuid import uuid4
from typing import List

from src.db.db import Base


class User(Base):
    __tablename__ = "users"

    uuid: Mapped[uuid4] = mapped_column(unique=True, default_factory=uuid4)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str]
    password: Mapped[str]
    comments: Mapped[List["Comment"]] = relationship(
        "Comment",
        back_populates="author",
    )

    posts: Mapped[List["Post"]] = relationship(
        secondary="users_posts_associations",
        back_populates="authors",
        uselist=True,
    )


class UserPostAssociation(Base):
    __tablename__ = "users_posts_associations"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )
    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id", ondelete="CASCADE"),
    )
