from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Не тот url/wrong url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"

    def  register_new_user(self,email, password):
        input1 = self.browser.find_element(*LoginPageLocators.EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION)
        button.click()
