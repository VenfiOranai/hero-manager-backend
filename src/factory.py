from flask import Flask

from src.config import Config


def create_app(config: Config = Config) -> Flask:
    app = Flask(__name__)

    app.config.from_object(config)

    return app
