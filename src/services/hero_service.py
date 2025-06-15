# services.py
from src.database.models.hero_model import HeroModel
from src.database.models.power_model import PowerModel
from src.controllers.models.new_hero import NewHero
from src.database.queries.power_queries import get_hero_powers


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

        self.session.commit()
        self.session.refresh(hero)
        return hero

    def retire_hero(self, hero_id: int) -> None:
        hero = self.session.query(HeroModel).filter_by(id=hero_id).first()
        if hero:
            hero.is_retired = True
            self.session.commit()

    def update_hero_powers(self, hero_id: int, new_powers: list[str]) -> None:
        if not new_powers:
            pass

        hero = self.session.query(HeroModel).filter_by(id=hero_id).first()
        hero_powers = get_hero_powers(hero_id)

        existing_powers = {power.name for power in hero_powers}
        new_powers_set = set(new_powers)

        for power_name in new_powers_set - existing_powers:
            self.session.add(PowerModel(name=power_name, hero_id=hero_id))

        for power in hero.powers:
            if power.name not in new_powers_set:
                self.session.delete(power)

        self.session.commit()
