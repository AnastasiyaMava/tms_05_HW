import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:

    def test(self):
        dr = webdriver.Chrome('/home/anastasiya/tms_05_HW/Locators/chromedriver')
        dr.get("http://the-internet.herokuapp.com/windows")
        dr.maximize_window()

        dr.find_element(By.XPATH, '//*[@id="content"]/div/a').click()

        main_window = dr.current_window_handle
        # dr.execute_script("window.open('http://the-internet.herokuapp.com/windows/new')")
        #dr.find_element(By.CLASS_NAME, "example")
        new_window = [window for window in dr.window_handles if window != main_window][0]
        dr.switch_to.window(new_window)
        time.sleep(5)

        dr.close()
        dr.switch_to_window(main_window)
