import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginCase(unittest.TestCase):
    driver = None
    email = 'matyshava@gmail.com'
    password = "Powerhou12"
    web_url = 'http://automationpractice.com/'

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome('/home/anastasiya/tms_05_HW/Selenium/chromedriver')
        cls.driver.maximize_window()
        cls.driver.get(cls.web_url)
        cls.driver.implicitly_wait(15)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()

    def login(self):
        self.driver.find_element(by=By.CLASS_NAME, value="login").click()
        self.driver.find_element(by=By.ID, value='email').send_keys(self.email)
        self.driver.find_element(by=By.ID, value="passwd").send_keys(self.password)
        self.driver.find_element(by=By.ID, value="SubmitLogin").click()

    def test_success(self):
        self.login()
        time.sleep(3)
        link = self.driver.find_element(by=By.CLASS_NAME, value='info-account')
        self.assertTrue('Welcome to your account.' in link.text)


if __name__ == '__main__':
    unittest.main()
