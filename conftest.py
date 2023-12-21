import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get_window_position()
    yield driver
    driver.quit()
