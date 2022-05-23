import pickle
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://www.saucedemo.com/'


@pytest.fixture()
def browser():
    browser = webdriver.Chrome('/home/anastasiya/tms_05_HW/chromedriver')
    browser.maximize_window()
    browser.implicitly_wait(10)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    log = browser.find_element(By.ID, 'user-name')
    log.send_keys('standard_user')
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.NAME, 'login-button').click()

    pickle.dump(browser.get_cookies(), open('session', 'wb'))


def test_1(login, browser):
    for cookie in pickle.load(open("session", "rb")):
        browser.add_cookie(cookie)

    logo = browser.find_element(By.CLASS_NAME, 'title')
    assert logo.text == 'PRODUCTS'


def test_2(browser):
    browser.delete_all_cookies()
    browser.refresh()
    log_logo = browser.find_element(By.CLASS_NAME, 'login_password')
    assert log_logo.text == 'Password for all users:\nsecret_sauce'
