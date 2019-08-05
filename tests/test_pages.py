async def test_index(test_cli):
    resp = await test_cli.get('/')
    assert resp.status == 200
    data = await resp.text()
    assert '<title>squash</title>' in data
