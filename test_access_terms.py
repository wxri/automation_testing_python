import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Access_terms(unittest.TestCase):
    CONTACT_INFO = (By.LINK_TEXT, "Contact")
    TERMS_INFO = (By.LINK_TEXT, "Termeni si conditii")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    # test 6 - accesarea rubricii "Termeni si conditii"
    def test_access_terms(self):
        self.chrome.find_element(*self.CONTACT_INFO).click()
        self.chrome.find_element(*self.TERMS_INFO).click()
        current_text = current_text = self.chrome.find_element(By. CLASS_NAME, "title-article").text
        valid_message = []
        if current_text != None:
            valid_message.append(current_text)
            assert valid_message == ["Termeni si conditii"]
        else: print("Terms and conditions page was not found")