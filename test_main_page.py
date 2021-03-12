from pages.main_page import MainPage


class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self):
        MainPage()\
            .open()\
            .go_to_login_page()\
            .should_be_login_page()

    def test_guest_should_see_login_link(self):
        MainPage()\
            .open()\
            .should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page():
    MainPage()\
        .open()\
        .go_to_basket_page()\
        .should_not_be_products_in_basket()\
        .should_be_message_that_basket_is_empty()
