from base_page import BasePage

class LoginPage(BasePage):
    def user_field(self, user):
        field = self.find_element(*LoginPageLocators.user)
        field.send_keys(user)
        return field

    def pass_field(self, passwd):

