import pytest
from squash.app import create_app


@pytest.yield_fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def test_cli(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app))


async def test_index(test_cli):
    resp = await test_cli.get('/api/v1/hello')
    assert resp.status == 200
    json_data = await resp.json()
    assert json_data == {'hello': 'world'}
