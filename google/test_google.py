import pytest
import time

import selenium.common.exceptions as selenium_exceptions
from selenium import webdriver


@pytest.fixture(scope='class')
def web_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--remote-debugging-port=9222')
    retry_count = 0
    while True:
        try:
            driver = webdriver.Chrome(chrome_options=chrome_options,
                                      executable_path='./chromedriver')
            driver.get("https://www.google.com/")
            driver.implicitly_wait(10)
        except selenium_exceptions.WebDriverException as web_error:
            if retry_count > 5:
                raise RuntimeError(web_error)

            retry_count += 1

            try:
                time.sleep(2)
            except Exception as e:
              print(e.message)
            continue

    yield driver
    driver.quit()


class TestGoogle:

    def test_url(self, web_driver):
        current_url = web_driver.current_url
        assert current_url == "https://www.google.com/"
