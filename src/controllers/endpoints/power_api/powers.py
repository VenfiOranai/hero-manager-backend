from flask import request

from src.database.database import session
from flask_api import status

from src.controllers.endpoints.power_api.output_schemas import GetHeroPowerOutputSchema
from src.controllers.models.update_hero_powers import UpdateHeroPowers
from src.controllers.utils.base_api import BaseApi
from src.database.queries.power_queries import get_hero_powers
from src.services.hero_service import HeroService


class PowersApi(BaseApi):
    def get(self, hero_id: int):
        return [GetHeroPowerOutputSchema(id=power.id, name=power.name, hero_id=power.hero_id).model_dump_json()
                for power in get_hero_powers(hero_id)], status.HTTP_200_OK

    def put(self, hero_id: int):
        hero_service = HeroService(session)

        hero_powers = UpdateHeroPowers(**request.get_json(force=True))
        hero_service.update_hero_powers(hero_id, hero_powers.powers)
        session.commit()

        return {"message": "Powers updated"}, status.HTTP_200_OK

