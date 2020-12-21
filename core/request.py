# coding: utf-8
from abc import ABC


class ABCRequest(ABC):
    pass


class InvalidRequest(ABCRequest):
    def __init__(self) -> None:
        super().__init__()
        self.errors = list()

    def add_error(self, parameter: str, message: str) -> None:
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self) -> bool:
        return bool(self.errors)
