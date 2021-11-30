from typing import Type

from database.repositories.base import BaseRepository
from database.models.teams import Team
from schema.teams import InTeamSchema, OutTeamSchema


class TeamsRepository(BaseRepository[InTeamSchema, OutTeamSchema, Team]):
    @property
    def _in_schema(self) -> Type[InTeamSchema]:
        return InTeamSchema

    @property
    def _schema(self) -> Type[OutTeamSchema]:
        return OutTeamSchema

    @property
    def _table(self) -> Type[Team]:
        return Team
