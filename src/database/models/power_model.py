from sqlalchemy import Column, Integer, String, ForeignKey

from src.database.database import SqlModel


class PowerModel(SqlModel):
    __tablename__ = 'Power'

    name = Column(String, nullable=False)
    hero_id = Column(Integer, ForeignKey('Hero.id'), nullable=False)
