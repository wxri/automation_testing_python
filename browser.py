from selenium import webdriver


class Browser():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(3)