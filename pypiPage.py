from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from page import BasePage


class pypiMainPage(BasePage):
    SEARCH_FIELD = (By.CLASS_NAME, "search-form__search")

    def __init__(self, browser):
        super().__init__(browser)

    def pypiSearch(self, keywords):
        self.find_an_element(pypiMainPage.SEARCH_FIELD).send_keys(keywords + Keys.RETURN)
