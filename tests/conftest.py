import pytest
import pytest_asyncio
from fastapi import BackgroundTasks
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.repositories.comment import get_comment_repository
from src.schemas.comment import CommentCreateSchema
from src.services.comment import get_comment_service
from src.repositories.post import get_post_repository
from src.schemas.post import PostCreateSchema
from src.services.post import get_post_service
from src.repositories.user import get_user_repository
from src.schemas.user import UserCreateSchema
from src.services.user import get_user_service
from src.db.db import Base, settings

engine = create_async_engine("postgresql+asyncpg://user:123@localhost:5432/test")
async_session = async_sessionmaker(engine, expire_on_commit=False)

@pytest_asyncio.fixture
async def create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def session(create):
    async with async_session() as session:
        yield session
        await session.rollback()


@pytest_asyncio.fixture
async def create_user(session):
    service = get_user_service(get_user_repository(session, settings))
    user = UserCreateSchema(
        username="JohnDoe",
        email="johndoe@gmail.com",
        password="johndoecool"
    )
    result = await service.create_one(user)
    yield result


@pytest_asyncio.fixture
async def create_post(session):
    service = get_post_service(get_post_repository(session, settings))
    post = PostCreateSchema(
        title="Very interesting topic",
        content="Content",
        author_id=1,
        is_auto_response=True,
        auto_response_delay=5,
    )
    result = await service.create_one(post)
    yield result



@pytest_asyncio.fixture
async def create_comments(session, create_user, create_post):
    contents = (
        "This topic is so fucking annoying",
        "I really love your speach",
        "Why is this motherfucker still live in our country?",
        "This bitch is a real cunt"
    )

    for content in contents:
        service = get_comment_service(get_comment_repository(session, settings))
        comment = CommentCreateSchema(
            content=content,
            author_id=create_user.id,
            post_id=create_post.id,
        )
        await service.create_one(comment, BackgroundTasks())
