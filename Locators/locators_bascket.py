from selenium.webdriver.common.by import By


class LocatorsBascket:
    logo = (By.CLASS_NAME, 'login_logo')
    menu = (By.ID, 'react-burger-menu-btn')
    card = (By.CLASS_NAME, 'title')
    qty = (By.CLASS_NAME, 'cart_quantity')
    item_name = (By.CLASS_NAME, 'inventory_item_name')
    remove = (By.CLASS_NAME, 'btn btn_secondary btn_small cart_button')
    cuntin_button = (By.ID, 'continue-shopping')
    checkout = (By.ID, 'checkout')
    twitter = (By.CLASS_NAME, 'social_twitter')
    facebook = (By.CLASS_NAME, 'social_facebook')
    linkedin = (By.CLASS_NAME, 'social_linkedin')