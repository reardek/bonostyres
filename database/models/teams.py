from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

from database.base import Base


class Team(Base):
    __tablename__ = 'team'

    name = Column(String, nullable=False)
    drivers = relationship('Driver', back_populates='team', passive_deletes=True)
