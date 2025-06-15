from flask import request

from database.database import session

from src.controllers.models.update_hero_powers import UpdateHeroPowers
from src.controllers.utils.base_api import BaseApi
from src.database.queries.power_queries import get_hero_powers
from src.services.hero_service import HeroService


class PowersApi(BaseApi):
    def get(self, hero_id: int):
        return [power for power in get_hero_powers(hero_id)]

    def put(self, hero_id: int):
        hero_service = HeroService(session)

        hero_powers = UpdateHeroPowers(**request.get_json(force=True))
        hero_service.update_hero_powers(hero_id, hero_powers.powers)

