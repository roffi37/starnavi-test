from fastapi import Depends

from src.services.base import BaseService
from src.repositories.user import get_user_repository, UserRepository


class UserService(BaseService):
    pass


def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)
