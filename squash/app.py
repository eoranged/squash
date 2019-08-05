from jinja2 import Environment, PackageLoader
from sanic import Sanic
from sanic.response import html, json


def create_app():
    app = Sanic(__name__)

    env = Environment(loader=PackageLoader('squash', 'templates'))

    @app.route('/')
    async def index(request):
        template = env.get_template('index.html')
        html_content = template.render(title='squash')
        return html(html_content)

    @app.route('/api/v1/hello')
    async def test(request):
        return json({'hello': 'world'})

    return app
