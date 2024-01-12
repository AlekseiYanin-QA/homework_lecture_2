import pytest
from selene import browser


@pytest.fixture()
def browser_scale():
    browser.config.window_width = 800
    browser.config.window_height = 600