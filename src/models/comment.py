from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base


class Comment(Base):
    __tablename__ = "comments"

    content: Mapped[str]
    author: Mapped["User"] = mapped_column(ForeignKey("posts.id"))
    author_id: Mapped[int] = relationship(
        "User",
        back_populates="comments",
    )
    likes: Mapped[int]
    dislikes: Mapped[int]
