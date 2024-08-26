from abc import ABC

from pydantic import BaseModel
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository(ABC):

    def __init__(self, session: AsyncSession, settings: BaseModel, model):
        self.session = session
        self.settings = settings
        self.model = model

    async def get_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]

    async def get_one(self, id_):
        pass

    async def create_one(self, data):
        stmt = insert(self.model).values(data).returning(self.model)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar().to_read_model()

    async def update_one(self, id_, data):
        data = {key: value for key, value in data.items() if value is not None}
        stmt = update(self.model).values(data).filter_by(id=id_).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar().to_read_model()

    async def delete_one(self, id_):
        stmt = delete(self.model).filter_by(id=id_).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar().to_read_model()
