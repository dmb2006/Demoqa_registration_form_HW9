from selene import browser
import pytest

@pytest.fixture(scope="session", autouse=True)
def configuration_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()

