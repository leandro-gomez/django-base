def test_index_view(client, settings):
    response = client.get(path="/")
    assert response.status_code == 200
    assert settings.SITE_TITLE in str(response.content)
