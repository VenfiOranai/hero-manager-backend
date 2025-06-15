from flask_api import status

from database.database import session
from src.controllers.utils.base_api import BaseApi
from src.services.hero_service import HeroService


class RetireHeroApi(BaseApi):
    def put(self, hero_id: int) -> tuple[dict[str, str], int]:
        hero_service = HeroService(session)

        hero_service.retire_hero(hero_id)
        return {"message": "Hero retired successfully!"}, status.HTTP_200_OK
