from selenium.webdriver.common.by import By


class LocatorsProd:
    logo = (By.CLASS_NAME, 'login_logo')
    prod = (By.CLASS_NAME, 'title')
    basket = (By.ID, 'shopping_cart_container')
    menu = (By.ID, 'react-burger-menu-btn')
    filter = (By.CLASS_NAME, 'select_container')
    item_name = (By.CLASS_NAME, 'inventory_item_name')
    item_desc = (By.CLASS_NAME, 'inventory_item_desc')
    item_price = (By.CLASS_NAME, 'inventory_item_price')
    add_batton = (By.ID, 'add-to-cart-sauce-labs-backpack')
    item_img = (By.CLASS_NAME, 'inventory_item_img')
    twitter = (By.CLASS_NAME, 'social_twitter')
    facebook = (By.CLASS_NAME, 'social_facebook')
    linkedin = (By.CLASS_NAME, 'social_linkedin')