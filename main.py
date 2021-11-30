from fastapi import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.dependencies.db import get_db
from api.routes.user import user_router
from database.repositories.teams import TeamsRepository
from schema.teams import OutTeamSchema, InTeamSchema

app = FastAPI()

app.include_router(user_router)


@app.post("/", status_code=status.HTTP_201_CREATED, response_model=OutTeamSchema)
async def root(payload: InTeamSchema, session: AsyncSession = Depends(get_db)) -> OutTeamSchema:
    team_repository = TeamsRepository(session)
    team = await team_repository.create(payload)
    return OutTeamSchema(**team.dict())
