from selenium import webdriver
from googleSearchPage import googleSearchPage, googleFirstResult
from pypiPage import pypiMainPage
from glCareersPage import glCareersPage, glCareersResultPage

driver = webdriver.Chrome()

googleSearchPage = googleSearchPage(driver)
googleSearchPage.open_page(googleSearchPage.URL)
googleSearchPage.googleSearch("selenium install ubuntu python")

firstResult = googleFirstResult(driver)
firstResult.openFirstResult()

pypiMainPage = pypiMainPage(driver)
pypiMainPage.pypiSearch("amazon-selenium 0.1.2")

glCareersPage = glCareersPage(driver)
glCareersPage.open()
glCareersPage.searchCareers("QA")

glCareersResultPage = glCareersResultPage(driver)
print(glCareersResultPage.getFirst())

driver.close()
