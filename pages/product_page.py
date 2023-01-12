from .base_page import BasePage
from .locators import ProductPageLocators


class ProguctPage(BasePage):
    def add_to_basket(self):
        to_basket = self.browser.find_element(*ProductPageLocators.button)
        to_basket.click()

    def compare_price(self):
        price1 = self.browser.find_element(*ProductPageLocators.price_one).text
        price2 = self.browser.find_element(*ProductPageLocators.price_two).text
        assert price1 == price2, 'Price is another'

    def compare_name_book(self):
        price1 = self.browser.find_element(*ProductPageLocators.name_one).text
        price2 = self.browser.find_element(*ProductPageLocators.name_two).text
        assert price1 == price2, 'Name book is another'


