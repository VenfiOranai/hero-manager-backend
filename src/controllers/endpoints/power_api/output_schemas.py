from src.controllers.utils.base_api_model import BaseApiModel


class GetHeroPowerOutputSchema(BaseApiModel):
   id: int
   name: str
   hero_id: int
