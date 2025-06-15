from pydantic import ConfigDict

from src.controllers.utils.base_api_model import BaseApiModel


class UpdateHeroPowers(BaseApiModel):
    model_config = ConfigDict(from_attributes=True)

    powers: list[str] | None = None


