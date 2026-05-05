from selenium.webdriver.common.by import By


import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    yield driver
    driver.quit()

def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    assert "amazon" in driver.title, 'Title for amazon is not correct'
    print("\n Opened Amazon Homepage. Title verified.")

def test_search_product(driver):
    wait = WebDriverWait(driver, 5)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabssearchtextbox")))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()
    # assert "wireless" in driver.current_url
    assert driver.current_url.__contains__('wireless')
    print("\n Search results page loaded successfully.")

def test_find_elements_amazon(driver):
    wait = WebDriverWait(driver, 15)

    # Single product title
    first_product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a h2 span")))
    print("\n First Product: ", first_product.text)

    product_titles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a h2 span")))
    print(f"\n Found {len(product_titles)} product titles on page one.\n")

    for i, title in enumerate(product_titles[:5], start=1):
        print(f"{i}. {title.text}")


    assert len(product_titles) > 0, "No products found on Amazon search results!"
    