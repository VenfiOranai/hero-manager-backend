from abc import ABC, abstractmethod


class BaseError(Exception, ABC):
    @abstractmethod
    @property
    def status_code(self) -> int:
        pass
