import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Log_in_invalid(unittest.TestCase):
    LOGIN_INIT = (By.CLASS_NAME, "box-cart-home")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "card-footer")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    # test 1 - Log In folosind credentiale invalide
    def test_log_in_invalid_credentials(self):
        self.chrome.find_element(*self.LOGIN_INIT).click()
        self.chrome.find_element(*self.EMAIL).send_keys("testwebtest@yahoo.com")
        self.chrome.find_element(*self.PASSWORD).send_keys("qwerty")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

        expected_URL = "https://www.quickmobile.ro/autentificare?message=invalid_account"
        try:
            assert self.chrome.current_url == expected_URL, "error message not found"
        except: raise AssertionError