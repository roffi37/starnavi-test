from fastapi import Depends

from src.exceptions import sign_in_error
from src.services.base import BaseService
from src.repositories.user import get_user_repository, UserRepository
from src.utils.security import hash_password
from src.utils.security import validate_password
from src.utils.auth import create_access_token


class UserService(BaseService):

    async def create_one(self, schema):
        data = schema.model_dump()
        password = data.pop("password")
        data["password"] = hash_password(password)
        return await self.repository.create_one(data)

    async def sign_in(self, schema) -> dict:
        data = schema.model_dump()
        email = data.pop("email")
        password = data.pop("password")
        user_password = await self.repository.get_one_by_email(email)
        if validate_password(password, user_password):
            return create_access_token(email)
        raise sign_in_error


def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)
