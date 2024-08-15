from abc import ABC

from src.repositories.base import BaseRepository


class BaseService(ABC):

    def __init__(self, repository):
        self.repository: BaseRepository = repository

    async def get_all(self):
        return await self.repository.get_all()

    async def get_one(self, id_):
        return await self.repository.get_one(id_)

    async def create_one(self, schema):
        data = schema.model_dump()
        return await self.repository.create_one(data)

    async def update_one(self, id_, schema):
        data = schema.model_dump()
        return await self.repository.update_one(id_, data)

    async def delete(self, id_):
        return await self.repository.delete_one(id_)
