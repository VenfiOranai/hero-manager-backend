from sqlalchemy import Column, Integer, String, ForeignKey

from src.database.database import SqlModel


class PowerModel(SqlModel):
    __tablename__ = 'Power'

    name = Column('Name', String, nullable=False)
    hero_id = Column('HeroId', Integer, ForeignKey('Hero.ID'), nullable=False)
