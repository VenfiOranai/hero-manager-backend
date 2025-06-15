from datetime import datetime

from src.controllers.models.hero_filters import HeroFilters
from src.database.models.hero_model import HeroModel
from src.database.models.power_model import PowerModel
from src.controllers.models.new_hero import NewHero
from src.database.queries.hero_queries import get_hero, get_heroes
from src.database.queries.power_queries import get_hero_powers
from src.errors.data_errors import NotFoundError


class HeroService:
    def __init__(self, session):
        self.session = session

    def create_hero(self, hero_data: NewHero) -> HeroModel:
        hero = HeroModel(
            name=hero_data.name,
            suit_color=hero_data.suit_color,
            has_cape=hero_data.has_cape,
            last_mission=hero_data.last_mission
        )
        self.session.add(hero)
        self.session.flush()

        for power_name in hero_data.powers:
            power = PowerModel(name=power_name, hero_id=hero.id)
            self.session.add(power)

        return hero

    def retire_hero(self, hero_id: int) -> None:
        hero = get_hero(hero_id)
        hero.is_retired = True
        self.session.commit()

    def get_hero_by_id(self, hero_id: int) -> HeroModel:
        return get_hero(hero_id)

    def get_heroes_by_filters(self, filters: HeroFilters) -> list[HeroModel]:
        return get_heroes(filters.suit_color, filters.has_cape, filters.name)

    def update_hero_powers(self, hero_id: int, new_powers: list[str]) -> None:
        if not new_powers:
            raise NotFoundError("There are no new powers to update!")

        get_hero(hero_id) # Validates if the hero exists
        hero_powers = get_hero_powers(hero_id)

        existing_powers = {power.name for power in hero_powers}
        new_powers_set = set(new_powers)

        for power_name in new_powers_set - existing_powers:
            self.session.add(PowerModel(name=power_name, hero_id=hero_id))

        for power in hero_powers:
            if power.name not in new_powers_set:
                self.session.delete(power)

    def update_hero_last_mission(self, hero_id: int, last_mission: datetime):
        hero = get_hero(hero_id)
        hero.last_mission = last_mission
