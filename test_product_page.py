from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.check_adding_item()
    page.solve_quiz_and_get_code()
    page.should_be_item_name()
    page.prises_should_be_equal()
    time.sleep(5)