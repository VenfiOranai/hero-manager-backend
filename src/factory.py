from flask import Flask

from src.config import Config
from src.controllers.router import make_routes


def create_app(config: Config = Config) -> Flask:
    app = Flask(__name__)

    app.config.from_object(config)

    make_routes(app)

    return app
