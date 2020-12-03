from selenium.webdriver.common.by import By
from page import BasePage


class glCareersPage(BasePage):
    URL = "https://www.globallogic.com/ua/careers/"

    SEARCH_FIELD = (By.ID, "by_keyword")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="hero"]/div/div/div/div/div/div/div[1]/form/div/button')
    ALLOW_COOKIE_BUTTON = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.open_page(glCareersPage.URL)
        self.click_element(glCareersPage.ALLOW_COOKIE_BUTTON)

    def searchCareers(self, vacancy):
        self.find_an_element(glCareersPage.SEARCH_FIELD).send_keys(vacancy)
        self.click_element(glCareersPage.SEARCH_BUTTON)

        return glCareersResultPage(self.browser)


class glCareersResultPage(BasePage):
    FIRST_RESULT = (By.CLASS_NAME, "mb-0")

    def __init__(self, browser):
        super().__init__(browser)

    def getFirst(self):
        firstResult = self.find_an_element(glCareersResultPage.FIRST_RESULT)
        return firstResult.text
