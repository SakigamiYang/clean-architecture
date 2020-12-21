# coding: utf-8
import typing

from domain.item import Item


class MemRepo:
    def __init__(self, entries: typing.List[typing.Mapping[str, typing.Any]] = None) -> None:
        self._entries = entries or list()

    def _check(self, element: typing.List[typing.Mapping[str, typing.Any]], key: str, value: typing.Any) -> bool:
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError(f'Operator {operator} is not supported')

        operator = f'__{operator}__'

        if key in ['price']:
            return getattr(element[key], operator)(float(value))
        if key in ['amount']:
            return getattr(element[key], operator)(int(value))
        return getattr(element[key], operator)(value)

    def list(self, filters: typing.Mapping[str, typing.Any] = None) -> typing.List[Item]:
        if not filters:
            result = self._entries
        else:
            result = list()
            result.extend(self._entries)
            for key, value in filters.items():
                result = [e for e in result if self._check(e, key, value)]

        return [Item.from_dict(r) for r in result]
