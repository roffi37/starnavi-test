from datetime import datetime, UTC

import pytest
from fastapi import BackgroundTasks

from src.config import get_settings
from src.repositories.comment import get_comment_repository
from src.schemas.comment import CommentCreateSchema, CommentSchema, DailyBreakdown
from src.services.comment import get_comment_service

settings = get_settings()



@pytest.mark.asyncio(loop_scope="session")
async def test_comments_repository_creating(session, create_user, create_post):
    service = get_comment_service(get_comment_repository(session, settings))
    comment = CommentCreateSchema(
        content="content",
        author_id=create_user.id,
        post_id=create_post.id,
    )
    result = await service.create_one(comment, BackgroundTasks())
    assert isinstance(result, CommentSchema)
    assert result.author_id == create_user.id
    assert result.post_id == create_post.id



@pytest.mark.asyncio(loop_scope="session")
async def test_daily_breakdown(session, create_comments):
    service = get_comment_service(get_comment_repository(session, settings))
    today = datetime.now(UTC).date().strftime("%Y-%m-%d")
    daily_breakdown = await service.get_daily_breakdown(today, today)
    assert isinstance(daily_breakdown, list)
    assert isinstance(daily_breakdown[0], DailyBreakdown)
    assert daily_breakdown[0].created_comments == 4
    assert daily_breakdown[0].blocked_comments == 3
