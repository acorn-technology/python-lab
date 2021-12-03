from flask import Flask
from flask_restx import Api

from count import api as count_api

# waitress-serve --call 'main:create_app'
def create_app():
    flask_app = Flask(__name__)
    api = Api(
        title='Count server API',
        version='1.0',
        description='',
    )
    api.add_namespace(count_api)
    api.init_app(flask_app)

    return flask_app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=8000)
