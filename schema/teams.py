from uuid import UUID

from schema.base import BaseSchema


class TeamSchemaBase(BaseSchema):
    name: str


class InTeamSchema(TeamSchemaBase):
    ...


class TeamSchema(TeamSchemaBase):
    id: UUID


class OutTeamSchema(TeamSchema):
    ...
