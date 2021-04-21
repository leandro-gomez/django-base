import pytest


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.headless = True
    return chrome_options
