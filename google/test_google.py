import warnings

import pytest
from selenium import webdriver


class ChromeDriverManager:
    def install(self):
        pass


@pytest.fixture(scope='class')
def web_driver():
    url = 'https://www.google.com/'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_argument('--disable-gpu')
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    browser.set_window_size(1920, 1080)

    browser.get(url)
    browser.implicitly_wait(2)
    yield browser
    browser.quit()


class TestGoogle:

    def test_url(self, browser):
        current_url = browser.current_url
        assert current_url == "https://www.google.com/"
