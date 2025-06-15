from abc import ABC, abstractmethod


class BaseError(Exception, ABC):
    @property
    @abstractmethod
    def status_code(self) -> int:
        pass
