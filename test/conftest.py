from turtle import update
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selene import browser
import pytest

from utils import attach


@pytest.fixture(scope="session", autouse=True)
def configuration_browser():
    load_dotenv()

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    # attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

# def configuration_browser():
#     browser.config.base_url = 'https://demoqa.com'
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#
#     yield
#
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     attach.add_video(browser)
#
#     browser.quit()

