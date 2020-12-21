# coding: utf-8
from core import response as resp
from core.usecase import UseCase
from repository.memrepo import MemRepo
from usecase.Item_request import ItemListRequest


class ItemUseCase(UseCase):
    def __init__(self, repo: MemRepo) -> None:
        self.repo = repo

    def process_request(self, request_object: ItemListRequest) -> resp.SuccessResponse:
        items = self.repo.list(filters=request_object.filters)
        return resp.SuccessResponse(data={'items': items})
