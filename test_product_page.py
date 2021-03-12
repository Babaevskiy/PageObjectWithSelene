import time

import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        email = str(time.time()) + '@fakemail.com'
        password = 'thisispassword'
        LoginPage()\
            .open()\
            .register_new_user(email, password)\
            .should_be_authorized_user()

    def test_user_can_add_product_to_basket(self):
        ProductPage()\
            .open()\
            .add_product_to_basket()\
            .should_be_message_about_add_product_to_basket()\
            .should_be_price_in_basket_equal_product_price()

    def test_user_cant_see_success_message(self):
        ProductPage()\
            .open()\
            .should_not_be_success_message()


@pytest.mark.parametrize('product', [
    'coders-at-work_207/?promo=offer0',
    'coders-at-work_207/?promo=offer1',
    'coders-at-work_207/?promo=offer2',
    'coders-at-work_207/?promo=offer3',
    'coders-at-work_207/?promo=offer4',
    'coders-at-work_207/?promo=offer5',
    'coders-at-work_207/?promo=offer6',
    'coders-at-work_207/?promo=offer7',
    'coders-at-work_207/?promo=offer8',
    'coders-at-work_207/?promo=offer9'
])
def test_guest_can_add_product_to_basket(product):
    ProductPage()\
        .open(product)\
        .add_product_to_basket()\
        .solve_quiz_and_get_code()\
        .should_be_message_about_add_product_to_basket()\
        .should_be_price_in_basket_equal_product_price()


def test_guest_cant_see_success_message():
    ProductPage()\
        .open()\
        .should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket():
    ProductPage()\
        .open()\
        .add_product_to_basket()\
        .should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket():
    ProductPage()\
        .open()\
        .add_product_to_basket()\
        .should_be_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page():
    product = 'the-city-and-the-stars_95/'
    ProductPage()\
        .open(product)\
        .should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page():
    product = 'the-city-and-the-stars_95/'
    ProductPage()\
        .open(product)\
        .go_to_login_page()\
        .should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page():
    product = 'the-city-and-the-stars_95/'
    ProductPage()\
        .open(product)\
        .go_to_basket_page()\
        .should_not_be_products_in_basket()\
        .should_be_message_that_basket_is_empty()
