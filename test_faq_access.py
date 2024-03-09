import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# test 7 - accesarea rubricii "Intrebari frecvente"
class FAQ_access(unittest.TestCase):
    FAQ_FIELD = (By. LINK_TEXT, "Intrebari frecvente")
    SCROLL = ("window.scrollTo(0, document.body.scrollHeight);")
    QUESTION_INDICATOR = (By.XPATH, '//div[@class="card-title card-suport-expand on" and contains(text(), "De ce s-a anulat comanda?")]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_faq_canceled(self):
        self.chrome.execute_script(self.SCROLL)
        self.chrome.find_element(*self.FAQ_FIELD).click()
        expected_url = "https://www.quickmobile.ro/suport/intrebari-frecvente"
        try:
            assert expected_url == self.chrome.current_url, "invalid url; the expected one was not found"
        except: raise AssertionError