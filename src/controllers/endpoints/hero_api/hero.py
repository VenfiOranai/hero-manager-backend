from src.controllers.endpoints.hero_api.output_schemas import GetHeroOutputSchema
from src.controllers.utils.base_api import BaseApi
from src.database.models import HeroModel
from src.database.queries.hero_queries import get_hero


class HeroApi(BaseApi):
    def get(self, hero_id: int):
        hero: HeroModel = get_hero(hero_id)

        return GetHeroOutputSchema(name=hero.name, suit_color=hero.suit_color, has_cape=hero.has_cape,
                                   last_mission=hero.last_mission, is_retired=hero.is_retired)

    def put(self):
        pass
