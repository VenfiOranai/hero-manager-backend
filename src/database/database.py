from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config import Config

Base = declarative_base()


class SqlModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)


engine = create_engine(Config.CONNECTION_STRING)
_session_maker = sessionmaker(engine)

session = _session_maker()
