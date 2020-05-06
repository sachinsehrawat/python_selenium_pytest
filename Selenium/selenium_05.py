from selenium import webdriver
import time

#Open Chrome Browser
driver =  webdriver.Chrome(executable_path='C:\Python Automation\Python Training\chromedriver.exe')

driver.get("https://www.makemytrip.com")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("[placeholder='From']").send_keys("melbou")
time.sleep(15)
cities = driver.find_elements_by_css_selector(".font14.appendBottom5.blackText")
print(len(cities))
for city in cities:
    if city.text == 'Melbourne, United States':
        city.click()
        break

#driver.find_element_by_id("toCity").click()

driver.find_element_by_css_selector("[placeholder='To']").send_keys("ams")
#time.sleep(5)

#driver.find_element_by_xpath("//div[text()='ZYA']").click()
