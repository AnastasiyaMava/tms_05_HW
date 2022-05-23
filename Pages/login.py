from Locators.locators_login import LocatorsLog
from Pages.fixture_BasePage import BasePage


class TestLogin(BasePage):

    def login(self):
        self.driver.find_element(*LocatorsLog.username).send_keys('standard_user')
        self.driver.find_element(*LocatorsLog.passwd).send_keys('secret_sauce')
        self.driver.find_element(*LocatorsLog.login_button).click()
