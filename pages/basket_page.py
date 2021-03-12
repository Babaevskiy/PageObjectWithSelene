from selene import be, have
from selene.support.shared.jquery_style import s


class BasketPage:

    def __init__(self):
        self.basket_items = s('.basket-items')
        self.message_about_empty_basket = s('#content_inner p')

    def should_not_be_products_in_basket(self):
        self.basket_items.should(be.not_.existing)
        return self

    def should_be_message_that_basket_is_empty(self):
        self.message_about_empty_basket.should(
            have.text('Your basket is empty. Continue shopping'))
        return self
