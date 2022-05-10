from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    Base_page_url = 'https://vk.com/'

    def __init__(self):
        self.driver = webdriver.Chrome('/home/anastasiya/tms_05_HW/pages/chromedriver')
        self.url = None

    def open(self, url):
        self.driver.get(url)

    def open_main_page(self):
        self.driver.get(self.Base_page_url)

    def find_element_locator(self, element_locators):
        element = self.driver.find_element(element_locators)
        WebDriverWait(self.driver, 10).until(element)
        return element
