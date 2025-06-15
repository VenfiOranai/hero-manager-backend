from flask import Flask
from flask_restful import Api

from src.controllers.endpoints.hero_api.hero import HeroApi
from src.controllers.endpoints.hero_api.heroes import HeroesApi
from src.controllers.endpoints.hero_api.retire_hero import RetireHeroApi
from src.controllers.endpoints.index import IndexApi
from src.controllers.endpoints.power_api.powers import PowersApi


def make_routes(app: Flask):
    api = Api(app)

    api.add_resource(IndexApi, '/')

    api.add_resource(HeroesApi, '/heroes')
    api.add_resource(HeroApi, '/heroes/<int:hero_id>')
    api.add_resource(RetireHeroApi, '/heroes/<int:hero_id>/retire')

    api.add_resource(PowersApi, '/heroes/<int:hero_id>/powers')
