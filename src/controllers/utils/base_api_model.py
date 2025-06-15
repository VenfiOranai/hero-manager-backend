from typing import Any

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class BaseApiModel(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True

    def model_dump(self, *args, **kwargs) -> dict[str, Any]:
        return super().model_dump(*args, by_alias=True, **kwargs)
