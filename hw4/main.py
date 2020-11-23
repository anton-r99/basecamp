from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    wait10 = WebDriverWait(driver, 10)
    driver.get("http://python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." in driver.page_source
    #driver.close()
