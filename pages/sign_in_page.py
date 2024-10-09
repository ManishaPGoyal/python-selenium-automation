#lesson7 homework
from pages.base_page import Page


class SignInPage(Page):

    def signin_form(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace='
                  'ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')


