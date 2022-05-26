import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def web_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path='/snap/bin/chromium.chromedriver')
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestGoogle:

    def test_url(self, web_driver):
        current_url = web_driver.current_url
        assert current_url == "https://www.google.com/"
