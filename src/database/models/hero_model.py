from sqlalchemy import Column, String, Boolean, DateTime

from src.database.database import SqlModel


class HeroModel(SqlModel):
    __tablename__ = 'Hero'

    name = Column('Name', String, nullable=False)
    suit_color = Column('SuitColor', String, nullable=False)
    has_cape = Column('HasCape', Boolean, nullable=False)
    last_mission = Column('LastMission', DateTime, nullable=True)
    is_retired = Column('IsRetired', Boolean, default=False)
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "suit_color": self.suit_color,
            "has_cape": self.has_cape,
            "is_retired": self.is_retired,
            "last_mission": self.last_mission.isoformat() if self.last_mission else None,
        }
