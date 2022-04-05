from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException

class BasketPage(BasePage):

    def go_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_button.click()

    def should_not_be_supplies(self):
        assert self.is_not_element_present(*BasketPageLocators.SUPPLIES_AREA), \
            "Success message is presented, but should not be"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "Message isn't presented"