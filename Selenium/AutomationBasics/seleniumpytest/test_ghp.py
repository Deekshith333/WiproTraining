import time
from distutils.command.check import check

from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle = driver.title
    assert pagetitle == 'Goggle', 'Google Home Page Not Loaded'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT, 'Business').click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.title_contains('Business'))
    assert 'business' in driver.title, 'Business Page Not Loaded - Title ccheck'
    assert 'business' in driver.current_url, 'Business Page Not Loaded - URL check'
    check.equal('business', driver.title, 'Business Page Not Loaded - Title check')
    check.is_in("business", driver.current_url, "Business Page Not Loaded - URL check")
