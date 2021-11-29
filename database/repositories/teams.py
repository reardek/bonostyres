from typing import Type

from database.repositories.base import BaseRepository
from database.models.teams import Team
from schema.teams import InTeamSchema, OutTeamSchema, TeamSchema


class TeamsRepository(BaseRepository[InTeamSchema, OutTeamSchema, Team]):
    @property
    def _in_schema(self) -> Type[InTeamSchema]:
        return InTeamSchema

    @property
    def _schema(self) -> Type[TeamSchema]:
        return TeamSchema

    @property
    def _table(self) -> Type[Team]:
        return Team