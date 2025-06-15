from flask_api import status
from flask_restful import Resource


class IndexApi(Resource):
    def get(self):
        return 'Running Hero Manager Backend', status.HTTP_200_OK
