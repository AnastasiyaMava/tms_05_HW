from selenium.webdriver.common.by import By


class LocatorsLog:
    logo = (By.CLASS_NAME, 'login_logo')
    username = (By.ID, 'user-name')
    passwd = (By.ID, 'password')
    login_button = (By.NAME, 'login-button')

