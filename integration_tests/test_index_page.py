"""
Home page integration tests
"""
import pytest


@pytest.mark.nondestructive
def test_index_page(selenium, base_url):
    """
    Test the home page is accessible
    """
    selenium.get(f"{base_url}/")
