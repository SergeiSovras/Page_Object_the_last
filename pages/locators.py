from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, '#id_registration-password2')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    ITEM_NAME2 = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    MESSAGE = (By.XPATH, "//strong[contains(text(), 'Deferred benefit offer')]")
    PRICE = (By.XPATH, "//p[contains(text(), 'Your basket total is now')]/strong")
    PRICE_ITEM = (By.XPATH, "//p[contains(@class, 'price_color')]")