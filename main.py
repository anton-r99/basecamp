from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('chromedriver')

driver.get("https://google.com")
keywords = "selenium install ubuntu python"

driver.find_element_by_name("q").send_keys(keywords + Keys.RETURN)

pypi = driver.find_element_by_partial_link_text("pypi")
pypi.click()

pypiSearchId = driver.find_element_by_class_name("search-form__search")
pypiSearchId.send_keys("selenium" + Keys.RETURN)

second_result = driver.find_element_by_partial_link_text("amazon-selenium 0.1.2")
second_result.click()

driver.get("https://www.globallogic.com/ua/careers/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
    )
finally:
    glSearchField = driver.find_element_by_class_name("form-control")
    glSearchField.send_keys("QA" + Keys.RETURN)
    driver.close()



