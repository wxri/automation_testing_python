import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Log_in_out(unittest.TestCase):
    LOGIN_INIT = (By.CLASS_NAME, "box-cart-home")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "card-footer")
    LOGOUT_BUTTON = (By.PARTIAL_LINK_TEXT, "Delogare")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    # test 2 - Log In folosind credentiale valide
    def test_log_in_valid(self):
        self.chrome.find_element(*self.LOGIN_INIT).click()
        self.chrome.find_element(*self.EMAIL).send_keys("testwebtest@yahoo.com")
        self.chrome.find_element(*self.PASSWORD).send_keys("nuamparola1234")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected_URL = "https://www.quickmobile.ro/cont?loggedin=1"
        try:
            assert self.chrome.current_url == expected_URL
        except: raise AssertionError

    # test 3 - Verificare Log Out
    def test_log_out(self):
        self.chrome.find_element(*self.LOGIN_INIT).click()
        self.chrome.find_element(*self.EMAIL).send_keys("testwebtest@yahoo.com")
        self.chrome.find_element(*self.PASSWORD).send_keys("nuamparola1234")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        self.chrome.find_element(By.LINK_TEXT, "Informatii cont").click()
        log_out_indicator = self.chrome.find_element(By.CLASS_NAME, "sidebar-subtitle").text
        expected_log_out_indicator = "Salut! Intra in cont pentru a accesa mai rapid cele mai noi tehnologii smart."
        try:
            assert expected_log_out_indicator == log_out_indicator, "log out indicator not found"
        except: raise AssertionError