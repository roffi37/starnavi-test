from datetime import datetime, UTC
import pytest
from fastapi import HTTPException

from src.db.db import settings
from src.repositories.post import get_post_repository
from src.schemas.post import PostCreateSchema, PostSchema
from src.services.post import get_post_service



@pytest.mark.asyncio(loop_scope="session")
async def test_comments_creating_with_not_existed_relation(session):
    service = get_post_service(get_post_repository(session, settings))
    post = PostCreateSchema(
        title="title",
        content="content",
        author_id=1,
        is_auto_response=False,
        auto_response_delay=0,
    )
    with pytest.raises(HTTPException):
        await service.create_one(post)



@pytest.mark.parametrize(
    "title, content, result_id, expected_result",
    [
        ("Artificial Intelligence", "Very interesting topic", 2, None),
        ("Bullshit", "I so fucking hate this one", 3, datetime.now(UTC).date()),
        ("Motherfucker", "I really love cats", 4, datetime.now(UTC).date()),
        ("Let's create the new world without racism", "niggers", 5, datetime.now(UTC).date()),
    ]
)
@pytest.mark.asyncio(loop_scope="session")
async def test_post_repository_creating(session, create_user, title, content, result_id, expected_result):
    service = get_post_service(get_post_repository(session, settings))
    post = PostCreateSchema(
        title=title,
        content=content,
        author_id=1,
        is_auto_response=False,
        auto_response_delay=0,
    )
    result = await service.create_one(post)
    assert result.id == 1
    assert isinstance(result, PostSchema)
    assert result.blocked_at == expected_result
