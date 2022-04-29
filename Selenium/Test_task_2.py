import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Account_test(unittest.TestCase):
    driver = None
    web_url = 'http://automationpractice.com/'

    login = 'ndobatovkinas@yandex.ru'
    password = "123456"
    first_name = "Anastasiya"
    last_name = "Dobatovkina"
    company = "QA-academy"
    address = "Lazo 13"
    city = "Vitebsk"
    postcode = "21000"
    phone = "+375258965544"
    address_alias = "Lazo 76"

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome('/home/anastasiya/tms_05_HW/Selenium/chromedriver')
        cls.driver.maximize_window()
        cls.driver.get(cls.web_url)
        cls.driver.implicitly_wait(15)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()

    def create_user(self):
        self.driver.find_element(by=By.CLASS_NAME, value="login").click()
        self.driver.find_element(by=By.ID, value="email_create").send_keys(self.login)
        self.driver.find_element(by=By.ID, value="SubmitCreate").click()
        self.driver.find_element(by=By.ID, value="id_gender2").click()
        self.driver.find_element(by=By.ID, value="customer_firstname").send_keys(self.first_name)
        self.driver.find_element(by=By.ID, value="customer_lastname").send_keys(self.last_name)
        self.driver.find_element(by=By.ID, value="passwd").send_keys(self.password)
        self.driver.find_element(by=By.ID, value="company").send_keys(self.company)
        self.driver.find_element(by=By.NAME, value="address1").send_keys(self.address)
        self.driver.find_element(by=By.ID, value="city").send_keys(self.city)
        state = Select(self.driver.find_element(by=By.ID, value="id_state"))
        state.select_by_value("2")
        self.driver.find_element(by=By.ID, value="postcode").send_keys(self.postcode)
        self.driver.find_element(by=By.ID, value="phone_mobile").send_keys(self.phone)
        self.driver.find_element(by=By.ID, value="alias").send_keys(self.address_alias)
        self.driver.find_element(by=By.ID, value="submitAccount").click()

    def information(self):
        self.driver.find_element(by=By.CLASS_NAME, value="login").click()
        self.driver.find_element(by=By.ID, value='email').send_keys(self.login)
        self.driver.find_element(by=By.ID, value="passwd").send_keys(self.password)
        self.driver.find_element(by=By.ID, value="SubmitLogin").click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="center_column"]/div/div[1]/ul/li[4]/a').click()

    def test_1_username(self):
        self.create_user()
        name_user = self.driver.find_element(by=By.XPATH, value='//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        self.assertTrue("Anastasiya Dobatovkina" in name_user.text)

    def test_2_firstname(self):
        self.information()
        name = self.driver.find_element(by=By.ID, value="firstname")
        self.assertEqual(self.first_name, name.get_attribute("value"))

    def test_3_surname(self):
        self.information()
        surname = self.driver.find_element(by=By.ID, value="lastname")
        self.assertEqual(self.last_name, surname.get_attribute("value"))


if __name__ == '__main__':
    unittest.main()
