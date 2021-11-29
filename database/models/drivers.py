from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class Driver(Base):
    __tablename__ = 'driver'

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    initial = Column(String(3), nullable=False)

    team_id = Column(UUID, ForeignKey('team.id', ondelete='CASCADE'))
    team = relationship('Team', back_populates="drivers")
