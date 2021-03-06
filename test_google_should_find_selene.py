import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(scope='session', autouse=True)
def browser_size():
    browser.config.window_width = 800
    browser.config.window_height = 600


def test_selene_in_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('selene: User-oriented Web UI browser tests in Python'))


def test_selene_in_google_fail():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Hello World'))