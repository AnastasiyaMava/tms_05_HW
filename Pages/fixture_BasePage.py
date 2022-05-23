from selenium import webdriver
import pytest


class BasePage:

    @pytest.fixture()
    def page(self):
        self.url = 'https://www.saucedemo.com/'
        self.driver = webdriver.Chrome('/home/anastasiya/tms_05_HW/chromedriver')
        self.driver.maximize_window()
        self.driver.get(self.url)
        yield
        self.driver.close()
        self.driver.quit()
