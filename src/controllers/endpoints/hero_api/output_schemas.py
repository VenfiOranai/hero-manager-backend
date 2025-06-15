from datetime import datetime

from pydantic import BaseModel


class GetHeroOutputSchema(BaseModel):
    id: int
    name: str
    suit_color: str
    has_cape: bool
    last_mission: datetime | None
    is_retired: bool
