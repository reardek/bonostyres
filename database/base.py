import datetime
import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.functions import now

@as_declarative()
class Base:
    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: DateTime = Column(DateTime, server_default=now())
    updated_at: DateTime = Column(DateTime, onupdate=datetime.datetime.now)

    __name__: str

    @declared_attr
    @classmethod
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
