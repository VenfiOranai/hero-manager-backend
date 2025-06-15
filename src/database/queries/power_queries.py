from src.database.database import session
from src.database.models.power_model import PowerModel


def get_hero_powers(hero_id: int) -> list[PowerModel]:
    return session.query(PowerModel).filter_by(hero_id=hero_id).all()
