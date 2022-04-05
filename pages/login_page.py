from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "LOGIN_EMAIL is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "LOGIN_PASSWORD is not presented"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "REGISTRATION_EMAIL is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1), "REGISTRATION_PASSWORD_1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2), "REGISTRATION_PASSWORD_2 is not presented"

    def register_new_user(self, email, password):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        password_field.send_keys(password)

        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        password_confirm_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
