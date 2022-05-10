from base_page import BasePage


class MainPage(BasePage):
    login_page = BasePage.Base_page_url + 'login'

    def open_login_page(self):
        self.open(self.login_page)
