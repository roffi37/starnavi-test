from fastapi import Depends
from typing import Annotated

from pydantic import BaseModel

from src.services.base import BaseService
from src.repositories.user import get_user_repository, UserRepository



class UserService(BaseService):

    async def get_all(self):
        return await self.repository.get_all()

    async def get_one(self, id_):
        return await self.repository.get_one(id_)

    async def create_one(self, schema: BaseModel):
        data = schema.model_dump()
        instance_id = await self.repository.create_one(data)
        return instance_id

    async def update_one(self, id_, data):
        return await self.repository.update_one(id_, data)

    async def delete(self, id_):
        return await self.repository.delete_one(id_)



UserRepositoryDependency = Annotated[UserRepository, Depends(get_user_repository)]

def get_user_service(repository: UserRepositoryDependency):
    return UserService(repository)
