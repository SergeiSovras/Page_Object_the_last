import math

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):

    def check_adding_item(self):
        self.should_be_add_button()
        self.solve_quiz_and_get_code()
        self.should_be_item_names()
        self.prises_should_be_equal()
        self.names_should_be_equal()

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

    def should_be_item_names(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), "Name isn't presented"
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME2), "Name2 isn't presented"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE), "Message isn't presented"

    def prises_should_be_equal(self):
        price1 = self.browser.find_element(*ProductPageLocators.PRICE).text
        price2 = self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text
        assert price1 == price2, "Values are not equal"

    def names_should_be_equal(self):
        name1 = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text,
        name2 = self.browser.find_element(*ProductPageLocators.ITEM_NAME2).text,
        #print(name1, name2)
        assert name1 == name2, "Names are not equal"

    def should_not_be_success_message(self): #Проверка, что элемента нет
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE), \
            "Success message isn't disappeared, but should be"

