from typing import Type
from uuid import uuid4

from pydantic.main import BaseModel
from database.models.users import User

from database.repositories.base import BaseRepository
from schema.user import InUserSchema, OutUserSchema


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

