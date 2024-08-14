from abc import ABC, abstractmethod

from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository(ABC):
    model = None

    def __init__(self, session: AsyncSession, settings: BaseSettings):
        self.session = session
        self.settings = settings

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def get_one(self, id_):
        pass

    @abstractmethod
    async def create_one(self, data):
        pass

    @abstractmethod
    async def update_one(self, id_, data):
        pass

    @abstractmethod
    async def delete_one(self, id_):
        pass
