from flask import request
from flask_api import status

from src.controllers.endpoints.hero_api.output_schemas import GetHeroOutputSchema
from src.controllers.utils.base_api import BaseApi
from src.database.database import session
from src.database.models import HeroModel
from src.database.queries.hero_queries import get_hero
from src.services.hero_service import HeroService


class HeroApi(BaseApi):
    def get(self, hero_id: int):
        hero: HeroModel = get_hero(hero_id)

        return GetHeroOutputSchema(id=hero.id, name=hero.name, suit_color=hero.suit_color, has_cape=hero.has_cape,
                                   last_mission=hero.last_mission, is_retired=hero.is_retired).model_dump_json(), status.HTTP_200_OK

    def put(self, hero_id: int):
        data = request.get_json()
        HeroService(session).update_hero_last_mission(hero_id, data.get('lastMission'))
        session.commit()
        return {'message': 'Updated successfully'}, status.HTTP_200_OK
