from .base_page import BasePage
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def sould_be_empty_basket(self):
        assert not self.is_not_element_present(*ProductPageLocators.basket_massage), "Basket is not empty"

    def sould_be_empty_basket_message(self):
        assert not self.is_disappeared(*ProductPageLocators.basket_massage), "Basket message is not presented"