from datetime import datetime

from src.controllers.utils.base_api_model import BaseApiModel


class GetHeroOutputSchema(BaseApiModel):
    id: int
    name: str
    suit_color: str
    has_cape: bool
    last_mission: datetime | None
    is_retired: bool
