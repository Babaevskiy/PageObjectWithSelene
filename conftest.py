import pytest

from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def close_browser():
    yield
    browser.quit()
