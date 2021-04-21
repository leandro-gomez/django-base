import pytest


@pytest.mark.nondestructive
def test_index_page(selenium, base_url):
    selenium.get(f"{base_url}/")
