from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id('name').send_keys("SSS")
driver.find_element_by_id('alertbtn').click()

alert = driver.switch_to.alert
print(alert.text)
assert 'SSS' in alert.text
alert.accept()

