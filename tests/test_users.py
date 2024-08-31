from datetime import datetime, UTC
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.user import get_user_repository
from src.schemas.user import UserCreateSchema, UserSchema
from src.services.user import get_user_service
from src.config import get_settings


settings = get_settings()

@pytest.mark.asyncio(loop_scope="session")
async def test_user_creating(session, create):
    service = get_user_service(get_user_repository(session, settings))
    user = UserCreateSchema(
        username="bob",
        email="bob@gmail.com",
        password="bob"
    )
    result = await service.create_one(user)
    assert isinstance(session, AsyncSession)
    assert isinstance(result, UserSchema)
    assert result.username == "bob"
    assert result.email == "bob@gmail.com"
    assert result.created_at.date() == datetime.now(UTC).date()
