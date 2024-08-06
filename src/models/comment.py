from sqlalchemy.orm import Mapped

from src.db.db import Base


class Comment(Base):
    __tablename__ = "comments"

    content: Mapped[str]
    author: Mapped["User"]
    likes: Mapped[int]
    dislikes: Mapped[int]
