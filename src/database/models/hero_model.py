from sqlalchemy import Column, String, Boolean, DateTime

from src.database.database import SqlModel


class HeroModel(SqlModel):
    __tablename__ = 'Hero'

    name = Column('Name', String, nullable=False)
    suit_color = Column('SuitColor', String, nullable=False)
    has_cape = Column('HasCape', Boolean, nullable=False)
    last_mission = Column('LastMission', DateTime, nullable=True)
    is_retired = Column('IsRetired', Boolean, default=False)
