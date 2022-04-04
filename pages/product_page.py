import math

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):

    def check_adding_item(self):
        self.should_be_add_button()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button isn't presented"

    def solve_quiz_and_get_code(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), "Name isn't presented"
        name1 = self.browser.find_element(*ProductPageLocators.ITEM_NAME),
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME2), "Name2 isn't presented"
        name2 = self.browser.find_element(*ProductPageLocators.ITEM_NAME),
        assert name1 == name2, "Names are not equal"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE), "Message isn't presented"

    def prises_should_be_equal(self):
        price1 = self.browser.find_element(*ProductPageLocators.PRICE)
        price2 = self.browser.find_element(*ProductPageLocators.PRICE_ITEM)
        assert price1.text == price2.text, "Values are not equal"

