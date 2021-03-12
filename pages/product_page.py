import math

from selene import be, have, query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from .login_page import LoginPage
from .basket_page import BasketPage


class ProductPage:

    def __init__(self):
        self.login_link = s('#login_link')
        self.basket_link = s('.btn-group .btn:nth-child(1)')
        self.basket_button = s('.btn-add-to-basket')
        self.product_name = s('.content h1')
        self.product_name_in_message = s('.alert:nth-child(1) strong')
        self.product_price = s('.product_main .price_color')
        self.product_price_in_message = s('.alert:nth-child(3) strong')

    def open(self, product=''):
        product = product or 'coders-at-work_207/'
        browser.open('http://selenium1py.pythonanywhere.com/en-gb/catalogue/'
                     + product).driver.maximize_window()
        return self

    def add_product_to_basket(self):
        self.basket_button.click()
        return self

    def go_to_login_page(self):
        self.login_link.click()
        return LoginPage()

    def go_to_basket_page(self):
        self.basket_link.click()
        return BasketPage()

    def should_be_message_about_add_product_to_basket(self):
        self.product_name_in_message\
            .should(have.text(self.product_name.get(query.text)))
        return self

    def should_be_price_in_basket_equal_product_price(self):
        self.product_price_in_message\
            .should(have.text(self.product_price.get(query.text)))
        return self

    def should_not_be_success_message(self):
        self.product_name_in_message.should(be.not_.existing)
        return self

    def should_be_success_message_is_disappeared(self):
        self.product_name_in_message.should(be.not_.existing)
        return self

    def should_be_login_link(self):
        self.login_link.should(be.existing)
        return self

    def solve_quiz_and_get_code(self):
        alert = browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        return self
