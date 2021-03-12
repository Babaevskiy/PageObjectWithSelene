from selene import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class LoginPage:

    def __init__(self):
        self.login_form = s('#login_form')
        self.registration_form = s('#register_form')
        self.registration_email_field = s('#id_registration-email')
        self.registration_password_field = s('#id_registration-password1')
        self.registration_password_field_2 = s('#id_registration-password2')
        self.registration_button = s('[name="registration_submit"]')
        self.user_icon = s('.icon-user')

    def open(self):
        browser.open('http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')\
            .driver.maximize_window()
        return self

    def register_new_user(self, email, password):
        self.registration_email_field.set_value(email)
        self.registration_password_field.set_value(password)
        self.registration_password_field_2.set_value(password)
        self.registration_button.click()
        return self

    def should_be_login_page(self):
        assert 'login' in browser.driver.current_url
        self.login_form.should(be.existing)
        self.registration_form.should(be.existing)
        return self

    def should_be_authorized_user(self):
        self.user_icon.should(be.visible)
        return self
