from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#Open Chrome Browser
driver =  webdriver.Chrome(executable_path='C:\Python Automation\Python Training\chromedriver.exe')

#Maximize browser window
driver.maximize_window()

#Open a web page
'''driver.get('https://rahulshettyacademy.com/angularpractice/')

#Static dropdown
gender = Select(driver.find_element_by_css_selector('#exampleFormControlSelect1'))

gender.select_by_index(1)

time.sleep(2)

gender.select_by_visible_text('Male')'''

#Checkboxes - selecting multiple

driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')

checkboxes = driver.find_elements_by_css_selector("[type='checkbox']")

for checkbox in checkboxes:
    checkbox.click()
    print(checkbox.get_attribute('value'))
    assert checkbox.is_selected()

#Radio buttons

buttons = driver.find_elements_by_name('radioButton')

buttons[2].click()

assert buttons[1].is_selected()
s
