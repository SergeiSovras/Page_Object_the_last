import math

from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException

class BasketPage(BasePage):

    #ef check_adding_item(self):
        #self.should_be_add_button()

    def go_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_LINK)  # * - значит, что мы передали именно пару.
        basket_button.click()

    def should_not_be_supplies(self): #Проверка, что товаров нет
        assert self.is_not_element_present(*BasketPageLocators.SUPPLIES_AREA), \
            "Success message is presented, but should not be"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "Message isn't presented"