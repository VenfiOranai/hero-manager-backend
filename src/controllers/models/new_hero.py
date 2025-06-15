from datetime import datetime
from pydantic import BaseModel


class NewHero(BaseModel):
    name: str
    suit_color: str
    has_cape: bool
    last_mission: datetime | None = None
    powers: list[str]