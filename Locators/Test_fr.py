import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testframe(unittest.TestCase):

    def test(self):
        dr = webdriver.Chrome('/home/anastasiya/tms_05_HW/Locators/chromedriver')
        dr.get("http://the-internet.herokuapp.com/iframe")
        dr.maximize_window()
        time.sleep(10)

       # dr.switch_to_frame(dr.find_element(By.TAG_NAME, "iframe"))
        a = dr.find_element(by=By.CLASS_NAME, value='tox-tbtn tox-tbtn--enabled')
        a.click()
        #a.send_keys("123456")

        # assert a.text == ''
