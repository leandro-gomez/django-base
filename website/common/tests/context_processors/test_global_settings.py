from unittest.mock import Mock

from website.common.context_processors import global_settings


def test_include_site_title(settings, faker):
    title = faker.word()
    settings.SITE_TITLE = title
    request = Mock()
    assert global_settings(request) == {"SITE_TITLE": title}
