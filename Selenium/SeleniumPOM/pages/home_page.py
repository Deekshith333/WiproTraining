from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 5)

    def type_search_input(self):
        search_box = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_box.clear()
        search_box.send_keys("wireless mouse")

