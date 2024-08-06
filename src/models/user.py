from sqlalchemy.orm import mapped_column, Mapped
from uuid import uuid4

from src.db.db import Base


class User(Base):
    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(unique=True, default_factory=uuid4)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str]
    password: Mapped[str]
