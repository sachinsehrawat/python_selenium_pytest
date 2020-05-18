#frame handling in python
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.familysearch.org/en/")

action = driver.Actionchains(driver)

