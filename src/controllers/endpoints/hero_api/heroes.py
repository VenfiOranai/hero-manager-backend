from flask import request

from src.controllers.endpoints.hero_api.output_schemas import GetHeroOutputSchema
from src.controllers.models.hero_filters import HeroFilters
from src.controllers.utils.base_api import BaseApi
from src.database.database import session
from src.services.hero_service import HeroService


class HeroesApi(BaseApi):
    def get(self):
        heroes = HeroService(session).get_heroes_by_filters(HeroFilters(**request.args))
        return [GetHeroOutputSchema(
            id=hero.id,
            name=hero.name,
            suit_color=hero.suit_color,
            has_cape=hero.has_cape,
            last_mission=hero.last_mission,
            is_retired=hero.is_retired,
        ).model_dump_json() for hero in heroes]

    def post(self):
        pass
