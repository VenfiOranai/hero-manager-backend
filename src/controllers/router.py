from flask import Flask
from flask_restful import Api

from src.controllers.index import IndexApi


def make_routes(app: Flask):
    api = Api(app)

    api.add_resource(IndexApi, '/')
