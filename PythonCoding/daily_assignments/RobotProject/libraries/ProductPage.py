from robot.libraries.BuiltIn import BuiltIn

class ProductPage:

    def get_product_price_by_name(self, product_name):

        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')

        xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']"

        price = seleniumlib.get_text(xpath)

        price = price.replace("$", "")

        return float(price)
