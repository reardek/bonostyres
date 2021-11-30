from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette import status
from api.dependencies.db import get_db
from database.repositories.user import UserToken, UsersRepository

from schema.user import InUserSchema, OutUserSchema


user_router = APIRouter(prefix="/user")


@user_router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserToken)
async def create_user(payload: InUserSchema, session: AsyncSession = Depends(get_db)) -> UserToken:
    user_repository = UsersRepository(session)
    token = await user_repository.create(payload)
    return UserToken(token="token")
