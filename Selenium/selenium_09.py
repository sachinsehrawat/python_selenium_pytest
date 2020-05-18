# handle multiple windows in selenium
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()

parent_window = driver.window_handles[0]

child_window = driver.window_handles[1]

driver.switch_to.window(child_window)

print(driver.find_element_by_xpath("//div/h3").text)

driver.switch_to.window(parent_window)

print(driver.find_element_by_xpath("//div/h3").text)

driver.quit()
