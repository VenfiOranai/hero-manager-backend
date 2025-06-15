from datetime import datetime

from pydantic import BaseModel


class GetHeroPowerOutputSchema(BaseModel):
   id: int
   name: str
   hero_id: int
