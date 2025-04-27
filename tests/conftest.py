import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from Config.config import *
import shutil


@pytest.fixture(scope="function")
def browser():
    """Setup and teardown for Selenium WebDriver."""
    options = Options()
    # options.add_argument('--headless')
    delete_all_directories()
    make_all_necssary_dir()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def make_all_necssary_dir():

    if not os.path.exists(f"{parent_dir}/Data"):
        os.makedirs(f"{parent_dir}/Data")

    if not os.path.exists(f"{parent_dir}/Data/ErrorScreenshot"):
        os.makedirs(f"{parent_dir}/Data/ErrorScreenshot")


def delete_all_directories():
    """
    Deletes all the necessary directories (Data and ErrorScreenshot) before starting.
    """
    error_screenshot_dir = os.path.join(str(parent_dir), "Data", "ErrorScreenshot")
    if os.path.exists(error_screenshot_dir):
        shutil.rmtree(error_screenshot_dir)

    # Deleting 'Data' directory if it exists
    data_dir = os.path.join(str(parent_dir), "Data")
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)

