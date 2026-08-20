import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.attach import (
    add_screenshot,
    add_page_source,
    add_video,
)

load_dotenv()

def pytest_addoption(parser):
    parser.addoption(
        "--site-url",
        default="https://demoqa.com/automation-practice-form",
        help="URL of the tested site"
    )

    parser.addoption(
        "--browser",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Browser name"
    )

    parser.addoption(
        "--browser-version",
        default="149.0",
        choices=("149.0", "148.0"),
        help="Browser version"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode"
    )

    parser.addoption(
        "--resolution",
        default="1920x1080",
        help="Browser resolution"
    )


@pytest.fixture(scope="session")
def site_url(request):
    return request.config.getoption("--site-url")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def browser_version(request):
    return request.config.getoption("--browser-version")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def resolution(request):
    return request.config.getoption("--resolution")


@pytest.fixture(scope="session")
def selenoid_url():
    login = os.getenv("SELENOID_LOGIN")
    password = os.getenv("SELENOID_PASSWORD")
    selenoid_host = os.getenv("SELENOID_URL")

    if not login:
        raise ValueError("SELENOID_LOGIN is not set")

    if not password:
        raise ValueError("SELENOID_PASSWORD is not set")

    if not selenoid_host:
        raise ValueError("SELENOID_URL is not set")

    # Убираем протокол, если он указан в .env
    selenoid_host = selenoid_host.removeprefix("https://")
    selenoid_host = selenoid_host.removeprefix("http://")

    # Убираем /wd/hub, если он случайно указан в .env
    selenoid_host = selenoid_host.removesuffix("/wd/hub")
    selenoid_host = selenoid_host.rstrip("/")

    return f"https://{login}:{password}@{selenoid_host}/wd/hub"


@pytest.fixture(scope="function")
def setup_browser(
    browser,
    browser_version,
    headless,
    resolution,
    selenoid_url
):
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    options.set_capability("browserName", browser)
    options.set_capability("browserVersion", browser_version)

    options.set_capability(
        "selenoid:options",
        {
            "name": "QA Guru test",
            "sessionTimeout": "60m",
            "screenResolution": f"{resolution}x24",
            "timeZone": "UTC",
            "labels": {
                "test": "registration_form"
            },
            "enableVNC": True,
            "enableVideo": True,
            "enableHAR": False,
            "enableLog": False,
        }
    )

    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options
    )

    yield driver

    # Allure attachments
    add_screenshot(driver)
    add_page_source(driver)
    add_video(driver)

    driver.quit()