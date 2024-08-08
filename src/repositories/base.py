from abc import ABC, abstractmethod

class BaseRepository(ABC):

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
