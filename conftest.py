import pytest
from selene import browser

@pytest.fixture()
def browser_open():
    browser.open('https://google.com')
    yield
    browser.quit()

@pytest.fixture()
def browser_scale():
    browser.config.window_width = 1200
    browser.config.window_height = 800
