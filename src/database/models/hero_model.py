from sqlalchemy import Column, String, Boolean, DateTime

from src.database.database import SqlModel


class HeroModel(SqlModel):
    __tablename__ = 'Hero'

    name = Column(String, nullable=False)
    suit_color = Column(String, nullable=False)
    has_cape = Column(Boolean, nullable=False)
    last_mission = Column(DateTime, nullable=True)
    is_retired = Column(Boolean, default=False)
