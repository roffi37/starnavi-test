from sqlalchemy.orm import Mapped

from src.db.db import Base


class Post(Base):
    __tablename__ = 'posts'

    title: Mapped[str]
    content: Mapped[str]
    authors: Mapped["User"]
    comments: Mapped["Comment"]
    tags: Mapped["Tag"]
