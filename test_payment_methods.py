import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Payment_methods(unittest.TestCase):
    MY_ORDER = (By.LINK_TEXT, "Comanda ta")
    PAYMENT_METHODS = (By.XPATH, '//div[@class="card-title card-suport-expand" and @data-toggle="expand" and @data-target="#article-suport-1972"]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    # test 8 - scenariu "ce metode de plata sunt acceptate?"
    def test_payment_methods(self):
        self.chrome.find_element(*self.MY_ORDER).click()
        self.chrome.find_element(*self.PAYMENT_METHODS).click()
        current_text = self.chrome.find_element(By.XPATH, '//div[contains(text(), "Metode de plata")]').text
        for text in current_text:
            assert "Metode de plata" in current_text, "expected text not found"