from schema.base import BaseSchema


class UserSchemaBase(BaseSchema):
    email: str


class InUserSchema(UserSchemaBase):
    password: str


class OutUserSchema(BaseSchema):
    ...
