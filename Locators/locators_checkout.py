from selenium.webdriver.common.by import By


class LocatorsCheckout:
    logo = (By.CLASS_NAME, 'login_logo')
    checkout_text = (By.CLASS_NAME, 'title')
    basket = (By.ID, 'shopping_cart_link')
    menu = (By.ID, 'react-burger-menu-btn')
    first_name = (By.ID, 'first-name')
    last_name = (By.ID, 'last-name')
    zip = (By.ID, 'postal-code')
    cancel_but = (By.NAME, 'cancel')
    cont_but = (By.ID, 'continue')
