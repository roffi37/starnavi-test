from fastapi import Depends
from typing import Annotated


from src.repositories.post import PostRepository, get_post_repository
from src.services.base import BaseService


class PostService(BaseService):
    pass


PostRepositoryDependency = Annotated[PostRepository, Depends(get_post_repository)]

def get_post_service(repository: PostRepositoryDependency):
    return PostService(repository)
