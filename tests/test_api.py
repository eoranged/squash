async def test_api_hello(test_cli):
    resp = await test_cli.get('/api/v1/hello')
    assert resp.status == 200
    json_data = await resp.json()
    assert json_data == {'hello': 'world'}
