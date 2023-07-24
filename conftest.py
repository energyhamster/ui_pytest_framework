import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager(version='114.0.5735.90').install())
    driver.maximize_window()
    yield driver
    driver.quit()
