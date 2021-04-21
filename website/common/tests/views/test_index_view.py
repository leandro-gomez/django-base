"""
Index view tests
"""


def test_index_view(client, settings):
    """
    Test the index view is working and rendering the SITE_TITLE
    """
    response = client.get(path="/")
    assert response.status_code == 200
    assert settings.SITE_TITLE in str(response.content)
