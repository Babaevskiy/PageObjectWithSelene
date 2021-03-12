from selene import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from .login_page import LoginPage
from .basket_page import BasketPage


class MainPage:

    def __init__(self):
        self.login_link = s('#login_link')
        self.basket_link = s('.btn-group .btn:nth-child(1)')

    def open(self):
        browser.open('http://selenium1py.pythonanywhere.com/en-gb/')\
            .driver.maximize_window()
        return self

    def go_to_login_page(self):
        self.login_link.click()
        return LoginPage()

    def go_to_basket_page(self):
        self.basket_link.click()
        return BasketPage()

    def should_be_login_link(self):
        self.login_link.should(be.existing)
        return self
