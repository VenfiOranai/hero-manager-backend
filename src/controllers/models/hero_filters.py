from src.controllers.utils.base_api_model import BaseApiModel


class HeroFilters(BaseApiModel):
    suit_color: str | None = None
    has_cape: bool | None = None
    name: str | None = None
