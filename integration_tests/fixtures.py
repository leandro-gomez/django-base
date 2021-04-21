"""
Integration tests fixtures.
Configure Firefox and Chrome
"""
import pytest


@pytest.fixture
def firefox_options(firefox_options):
    """
    Set Firefox Headless
    """
    firefox_options.headless = True
    return firefox_options


@pytest.fixture
def chrome_options(chrome_options):
    """
    Set Chrome Headless
    """
    chrome_options.headless = True
    return chrome_options
