from sanic import Sanic
from sanic.response import json


def create_app():
    app = Sanic(__name__)

    @app.route('/api/v1/hello')
    async def test(request):
        return json({'hello': 'world'})

    return app
