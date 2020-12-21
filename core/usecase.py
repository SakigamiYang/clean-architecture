# coding: utf-8
from abc import abstractmethod

from core import request as req, response as resp


class UseCase:
    def execute(self, request_object: req.ABCRequest):
        if isinstance(request_object, req.InvalidRequest):
            return resp.FailureResponse.build_from_invalid_request(request_object)
        try:
            return self.process_request(request_object)
        except BaseException as ex:
            return resp.FailureResponse.build_system_error(f'{ex.__class__.__name__}: {ex}')

    @abstractmethod
    def process_request(self, request_object: req.ABCRequest):
        pass
