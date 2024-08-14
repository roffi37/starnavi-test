from abc import ABC, abstractmethod

from src.repositories.base import BaseRepository


class BaseService(ABC):

    def __init__(self, repository):
        self.repository: BaseRepository = repository

    @abstractmethod
    async def get_all(self):
        return await self.repository.get_all()

    @abstractmethod
    async def get_one(self, id_):
        return await self.repository.get_one(id_)

    @abstractmethod
    async def create_one(self, data):
        return await self.repository.create_one(data)

    @abstractmethod
    async def update_one(self, id_, data):
        return await self.repository.update_one(id_, data)

    @abstractmethod
    async def delete(self, id_):
        return await self.repository.delete_one(id_)
