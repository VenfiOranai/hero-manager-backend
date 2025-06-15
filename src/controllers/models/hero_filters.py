from pydantic import BaseModel


class HeroFilters(BaseModel):
    suit_color: str | None = None
    has_cape: bool | None = None
    name_contains: str | None = None