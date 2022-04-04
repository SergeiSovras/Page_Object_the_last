from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "LOGIN_EMAIL is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "LOGIN_PASSWORD is not presented"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "REGISTRATION_EMAIL is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1), "REGISTRATION_PASSWORD_1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2), "REGISTRATION_PASSWORD_2 is not presented"