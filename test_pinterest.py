import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Pinterest_check(unittest.TestCase):
    PINTEREST_ICON = (By.XPATH, '//i[@class="fa fa-pinterest icon-footer"]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    # test 10 - scenariu accesare platforma de tip2 social media
    def test_pinterest_access(self):
        self.chrome.find_element(*self.PINTEREST_ICON).click()
        self.chrome.switch_to.window(self.chrome.window_handles[-1])
        expected_URL = "https://www.pinterest.com/quickmobile/"
        assert self.chrome.current_url == expected_URL, f"invalid URL: found -> {self.chrome.current_url}, instead of -> {expected_URL}"