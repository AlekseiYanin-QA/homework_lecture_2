import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_scale():
    browser.config.window_width = 1200
    browser.config.window_height = 800
    yield
    browser.quit()