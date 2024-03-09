import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Instagram_check(unittest.TestCase):
    INSTAGRAM_ICON = (By.XPATH, '//i[@class="fa fa-instagram icon-footer"]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    # test 9 - scenariu accesare platforma de tip1 social media
    def test_instagram_access(self):
        self.chrome.find_element(*self.INSTAGRAM_ICON).click()
        self.chrome.switch_to.window(self.chrome.window_handles[-1])
        expected_URL = "https://www.instagram.com/quickmobilero/"
        assert self.chrome.current_url == expected_URL, f"invalid URL: found -> {self.chrome.current_url}, instead of -> {expected_URL}"