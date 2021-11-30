from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

from database.base import Base


class User(Base):
    __tablename__ = 'user'

    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
