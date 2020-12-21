# coding: utf-8
import typing

from core.domainmodel import DomainModel


class Item(DomainModel):
    def __init__(self, id_: str, price: float, amount: int) -> None:
        super().__init__(id_)
        self.price = price
        self.amount = amount

    @classmethod
    def from_dict(cls, __m: typing.Mapping[str, typing.Any]) -> 'Item':
        return Item(__m['id'], __m['price'], __m['amount'])

    def to_dict(self):
        return {'id': self.id_, 'price': self.price, 'amount': self.amount}
