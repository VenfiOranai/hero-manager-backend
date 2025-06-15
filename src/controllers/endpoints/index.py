from flask_api import status

from src.controllers.utils.base_api import BaseApi
from src.errors.data_errors import NotFoundError


class IndexApi(BaseApi):
    def get(self):
        raise NotFoundError('baller')
        return 'Running Hero Manager Backend', status.HTTP_200_OK
