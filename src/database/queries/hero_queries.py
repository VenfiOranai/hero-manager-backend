from sqlalchemy.exc import NoResultFound

from src.database.database import session
from src.database.models.hero_model import HeroModel
from src.errors.data_errors import NotFoundError


def get_hero(hero_id: int) -> HeroModel:
    try:
        return session.query(HeroModel).filter_by(id=hero_id).one()
    except NoResultFound:
        raise NotFoundError(f'Hero with id {hero_id} does not exist')


def get_heroes(suit_color: str | None = None, has_cape: bool | None = None, name: str | None = None) -> list[HeroModel]:
    query = session.query(HeroModel)

    if suit_color is not None:
        query = query.filter_by(suit_color=suit_color)

    if has_cape is not None:
        query = query.filter_by(has_cape=has_cape)

    if name is not None:
        query = query.filter(HeroModel.name.like(f'%{name}%'))

    return query.all()
