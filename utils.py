import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from browser import Browser

class Utils(Browser):
    cookies_button = (By. XPATH, '//button[@onclick="closeCookie(\'HeaderCookie\')"]')
    def accept_cookies(self):
        try:
            self.chrome.find_element(*self.cookies_button).click()
        except:
            pass