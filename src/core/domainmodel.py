# coding: utf-8
from abc import ABC


class DomainModel(ABC):
    def __init__(self, id_: str) -> None:
        self.id_ = id_
