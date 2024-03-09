import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Cellphones_selection(unittest.TestCase):
    SHOP_MENU = (By. ID, "main-menu-toggle")
    CELLPHONES_FIELD = (By.LINK_TEXT, "Telefoane Mobile")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    # test 4 - selectarea categoriei "SHOP" + selectie "Telefoane mobile"
    def test_cellphones_selection(self):
        self.chrome.find_element(*self.SHOP_MENU).click()
        self.chrome.find_element(*self.CELLPHONES_FIELD).click()
        displayed_text = self.chrome.find_element(By.CLASS_NAME, "clear-style").text
        valid_messages = []
        if displayed_text:
            valid_messages.append(displayed_text)
            try:
                assert len(valid_messages) != 0
            except: raise AssertionError
        else:
            print ("Invalid condition")