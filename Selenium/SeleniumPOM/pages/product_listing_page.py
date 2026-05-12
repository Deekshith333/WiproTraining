from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class ProductListingPage:

    PRODUCT_TITLES = (By.CSS_SELECTOR, "a h2 span")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_product_title(self, driver):
        first_product = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))
        print("\nFirst Product:", first_product.text)

    def all_products(self, driver):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))
        print(f"\n Found {len(product_titles)} product titles on page one. \n")

        for i, title in enumerate(product_titles[:5], start=1):
            print(f"{i}, {title.text}")

        return len(product_titles) > 0

    def select_brand_filter(self):
        brand_filter = self.driver.find_element(*self.BRAND_FILTER)
        brand_filter.click()

    def check_product_titles_for_brand_filter(self, brandname):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))

        for title in product_titles:
            if not title.text.__contains__(brandname):
                return False
        return True

    def mensize_locator(selfself, mensize):
        MENSIZE_FILTER = (By.XPATH, "(//span[@class='a-List-item']/descendant::button[@value='" + mensize + "'])[1]")
        return MENSIZE_FILTER

    def select_mensize_filter(self, mensize):
        mensize_filter = self.driver.find_element(*self.mensize_locator(self.mensize_locator(mensize)))
        mensize_filter.click()

