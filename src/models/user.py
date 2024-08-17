from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List

from src.models.comment import Comment
from src.models.post import Post
from src.schemas.user import UserSchema
from src.db.db import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str]
    password: Mapped[str]
    comments: Mapped[List["Comment"]] = relationship(
        back_populates="author",
    )
    posts: Mapped[List["Post"]] = relationship(
        back_populates="author",
    )

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            email=self.email,
            username=self.username,
            password=self.password,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
