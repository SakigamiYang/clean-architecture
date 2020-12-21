# coding: utf-8
import typing

from flask import Blueprint, request, Response

from core.request import InvalidRequest
from repository.memrepo import MemRepo
from usecase.Item_request import ItemListRequest
from usecase.item_usecase import ItemUseCase

item_bp = Blueprint('item_bp', __name__)

item_1 = {'id': 'item-a', 'price': 11, 'amount': 10}
item_2 = {'id': 'item-b', 'price': 2.2, 'amount': 200}
item_3 = {'id': 'item-c', 'price': 333, 'amount': 3}


@item_bp.route('/items', methods=['GET'])
def items():
    filters = dict()

    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            filters[arg.replace('filter_', '')] = values

    if not isinstance(filters, typing.Mapping):
        req = InvalidRequest()
        req.add_error('filters', 'is not iterable')
    else:
        req = ItemListRequest(filters=filters)

    repo = MemRepo([item_1, item_2, item_3])
    usecase = ItemUseCase(repo)

    resp = usecase.execute(req)

    return Response(resp.to_json(),
                    status=200,
                    mimetype='application/json')
