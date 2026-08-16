import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope="function")
def setup_browser():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "149.0",
        "selenoid:options": {
            "name": "Manual session",
            "sessionTimeout": "60m",
            "screenResolution": "1920x1080x24",
            "timeZone": "UTC",
            "labels": {"manual": "true"},
            "enableVNC": True,
            "enableVideo": True,
            "enableHAR": False,
            "enableLog": False,
        },
    }

    options = Options()

    for key, value in capabilities.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor="https://qa_engineer:-aAb_-4gs53FD@selenoid.qa.guru/wd/hub",
        options=options,
    )

    yield driver

    attach.add_screenshot(driver)
    attach.add_page_source(driver)
    attach.add_console_logs(driver)
    attach.add_video(driver)

    driver.quit()