#frame handling in python
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")

driver.find_element_by_xpath("//body/p").clear()

driver.find_element_by_xpath("//body/p").send_keys("Sachin")

driver.switch_to.default_content()

print(driver.find_element_by_xpath("//div/h3").text)

