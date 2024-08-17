from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.schemas.comment import CommentSchema
from src.db.db import Base


class Comment(Base):
    __tablename__ = "comments"

    content: Mapped[str]
    likes: Mapped[int] = mapped_column(default=0)
    dislikes: Mapped[int] = mapped_column(default=0)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    is_blocked: Mapped[bool] = mapped_column(default=False)
    author: Mapped["User"] = relationship(
        back_populates="comments",
    )
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    post: Mapped["Post"] = relationship(
        back_populates="comments",
    )

    def to_read_model(self) -> CommentSchema:
        return CommentSchema(
            id=self.id,
            content=self.content,
            likes=self.likes,
            dislikes=self.dislikes,
            author_id=self.author_id,
            is_blocked=self.is_blocked,
            post_id=self.post_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
