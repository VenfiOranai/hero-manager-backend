from src.errors.base import BaseError


class NotFoundError(BaseError):
    status_code = 404
