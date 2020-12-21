# coding: utf-8
from flask import Flask

from api.item_api import item_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(item_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=20000, debug=True)
