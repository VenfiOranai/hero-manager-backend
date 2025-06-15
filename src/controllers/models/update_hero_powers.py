from datetime import datetime
from pydantic import BaseModel, ConfigDict


class UpdateHeroPowers(BaseModel):
   model_config = ConfigDict(from_attributes=True)

   hero_id: int
   powers: list[str] | None = None


