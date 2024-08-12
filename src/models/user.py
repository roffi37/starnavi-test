from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List

from src.db.db import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str]
    password: Mapped[str]
    comments: Mapped[List["Comment"]] = relationship(
        "Comment",
        back_populates="author"
    )
    posts: Mapped[List["Post"]] = relationship(
        "Post",
        back_populates="author"
    )
