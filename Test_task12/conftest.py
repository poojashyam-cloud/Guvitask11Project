import pytest
from selenium import webdriver

@pytest.fixture
def launch_guvi():
    driver = webdriver.Edge()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    return driver
