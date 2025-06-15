from flask_restful import Resource, abort

from src.errors.base import BaseError


def catch_custom_errors(f: callable):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseError as e:
            abort(e.status_code, message=str(e))

    return wrapper


class BaseApi(Resource):
    decorators = [catch_custom_errors]
