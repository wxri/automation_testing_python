import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Warranty_check(unittest.TestCase):
    EXTENDED_WARRANTY = (By.LINK_TEXT, "Garantie extinsa")
    STANDARD_WARRANTY = (By.LINK_TEXT, "Garantie standard")
    TEXT_INDICATOR = (By.XPATH, '//h2[contains(text(), "Garantie standard")]')


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    # test 11 - scenariu afisare informatii de tip "garantie standard"
    def test_standard_warranty(self):
        self.chrome.find_element(*self.EXTENDED_WARRANTY).click()
        self.chrome.find_element(*self.STANDARD_WARRANTY).click()
        current_text = self.chrome.find_element(*self.TEXT_INDICATOR).text
        expected_text = "Garantie standard"
        if current_text:
            assert current_text == expected_text
        else:
            return AssertionError