# coding: utf-8
import typing
from abc import ABC

import orjson

from core import request as req


class ResponseCode:
    __slots__ = ('code', 'message')

    def __init__(self, code, message):
        self.code = code
        self.message = message


class ResponseCodes:
    OK = ResponseCode(0, 'OK')
    PARAMETERS_ERROR = ResponseCode(100000, 'PARAMETERS_ERROR')
    RESOURCE_ERROR = ResponseCode(200000, 'RESOURCE_ERROR')
    SYSTEM_ERROR = ResponseCode(900000, 'SYSTEM_ERROR')


class ABCResponse(ABC):
    def __init__(self,
                 response_code: ResponseCode = ResponseCodes.OK,
                 data: typing.Any = None,
                 error: typing.Union[str, BaseException] = None) -> None:
        self.code = response_code.code
        self.message = response_code.message
        self.data = data
        self.error = self._format_error(error)

    @staticmethod
    def _format_error(error: typing.Union[str, BaseException]) -> str:
        if isinstance(error, BaseException):
            return f'{error.__class__.__name__}: {error}'
        return error

    def to_json(self) -> bytes:
        return orjson.dumps({
            'code': self.code,
            'message': self.message,
            'data': self.data,
            'error': self.error,
        })


class SuccessResponse(ABCResponse):
    def __init__(self, data=None) -> None:
        super().__init__(data=data)


class FailureResponse(ABCResponse):
    def __init__(self, response_code: ResponseCode, error: typing.Union[str, BaseException]) -> None:
        super().__init__(response_code=response_code, error=error)

    @classmethod
    def build_parameters_error(cls, error: typing.Union[str, BaseException]) -> 'FailureResponse':
        return cls(ResponseCodes.PARAMETERS_ERROR, error)

    @classmethod
    def build_resource_error(cls, error: typing.Union[str, BaseException]) -> 'FailureResponse':
        return cls(ResponseCodes.RESOURCE_ERROR, error)

    @classmethod
    def build_system_error(cls, error: typing.Union[str, BaseException]) -> 'FailureResponse':
        return cls(ResponseCodes.SYSTEM_ERROR, error)

    @classmethod
    def build_from_invalid_request(cls, invalid_request: req.InvalidRequest) -> 'FailureResponse':
        error = '\n'.join(f'{err["parameter"]}: {err["message"]}' for err in invalid_request.errors)
        return cls.build_parameters_error(error)
