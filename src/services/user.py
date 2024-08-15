from fastapi import Depends
from typing import Annotated

from src.services.base import BaseService
from src.repositories.user import get_user_repository, UserRepository



class UserService(BaseService):
    pass



UserRepositoryDependency = Annotated[UserRepository, Depends(get_user_repository)]

def get_user_service(repository: UserRepositoryDependency):
    return UserService(repository)
