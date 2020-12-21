# coding: utf-8
from core import request as req


class ItemListRequest(req.ABCRequest):
    def __init__(self, filters=None) -> None:
        super().__init__()
        self.filters = filters
