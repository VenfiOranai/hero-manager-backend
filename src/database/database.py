from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config import Config

_Base = declarative_base()


class SqlModel(_Base):
    id = Column(Integer, primary_key=True)


_engine = create_engine(Config.CONNECTION_STRING)
_session_maker = sessionmaker(_engine)

session = _session_maker()
