from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from page import BasePage


class googleSearchPage(BasePage):
    URL = "https://google.com"
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (
        By.CLASS_NAME,
        'gNO89b',
    )

    def __init__(self, browser):
        super().__init__(browser)

    def googleSearch(self, keywords):
        self.find_an_element(googleSearchPage.SEARCH_FIELD).send_keys(keywords + Keys.RETURN)


class googleFirstResult(BasePage):
    FIRST_RESULT = (By.PARTIAL_LINK_TEXT, "pypi")

    def __init__(self, browser):
        super().__init__(browser)

    def openFirstResult(self):
        self.find_an_element(googleFirstResult.FIRST_RESULT).click()
