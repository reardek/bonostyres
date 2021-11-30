from typing import Type
from uuid import uuid4
from logging import log

from pydantic.main import BaseModel
from database.models.users import User

from database.repositories.base import BaseRepository
from schema.user import InUserSchema, OutUserSchema

from sqlalchemy import select


class UserToken(BaseModel):
    token: str


class UsersRepository(BaseRepository[InUserSchema, OutUserSchema, User]):
    @property
    def _in_schema(self) -> Type[InUserSchema]:
        return InUserSchema

    @property
    def _schema(self) -> Type[OutUserSchema]:
        return OutUserSchema

    @property
    def _table(self) -> Type[User]:
        return User

    async def create_or_reject(self, in_user: InUserSchema):
        user_query = select(User).where(User.email == in_user.email)
        user = await self._db_session.execute(user_query)
        if user.fetchall():
            raise Exception(f"User with email {in_user.email} already exists")
        await self.create(in_user)
