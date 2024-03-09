import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Brand_sorting(unittest.TestCase):
    BRAND_FILTER = (By.CSS_SELECTOR, 'div.filter-title[data-target="#filterBox-3-2"]')
    SEARCH_BAR = (By.CSS_SELECTOR, "#filterBox-3-2 > input")
    SAMSUNG_FILTER = (By.CSS_SELECTOR, "#filter-3-2 > ul > li:nth-child(12) > div > a > label")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.quickmobile.ro/telefoane-mobile")

    def tearDown(self) -> None:
        self.chrome.quit()

    # test 5 - sortare telefoane mobile dupa brand-ul "SAMSUNG"
    def test_brand_sorting(self):
        self.chrome.find_element(*self.BRAND_FILTER).click()
        self.chrome.find_element(*self.SEARCH_BAR).send_keys("SAMSUNG")
        samsung_filter = WebDriverWait(self.chrome, 5).until(EC.element_to_be_clickable(self.SAMSUNG_FILTER))
        samsung_filter.click()
        WebDriverWait(self.chrome, 5).until(EC.url_to_be("https://www.quickmobile.ro/telefoane-mobile#filtre/marca-samsung"))
        expected_URL = "https://www.quickmobile.ro/telefoane-mobile#filtre/marca-samsung"
        try:
            assert self.chrome.current_url == expected_URL, 'expected page not found'
        except: raise AssertionError