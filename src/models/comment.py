from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base


class Comment(Base):
    __tablename__ = "comments"

    content: Mapped[str]
    likes: Mapped[int]
    dislikes: Mapped[int]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(
        back_populates="comments",
    )
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    post: Mapped["Post"] = relationship(
        back_populates="comments",
    )
