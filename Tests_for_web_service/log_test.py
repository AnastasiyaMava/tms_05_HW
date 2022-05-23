from Locators.locators_product_page import LocatorsProd
from Pages.login import TestLogin
from Pages.fixture_BasePage import BasePage


class TestLog(TestLogin, BasePage):

    def test_1(self, page):
        self.login()
        title = self.driver.find_element(*LocatorsProd.prod)
        assert title.text == 'PRODUCTS'
