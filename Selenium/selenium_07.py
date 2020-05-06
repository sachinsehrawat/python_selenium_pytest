from selenium import webdriver
driver = webdriver.Chrome()
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#implicit wait
'''driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
driver.find_element_by_css_selector("button.search-button").click
time.sleep(3)
buttons = driver.find_elements_by_xpath("//div[@class='product-action'] /button")
print(len(buttons))
assert len(buttons) == 3
for button in buttons:
    button.click()
driver.find_element_by_xpath("//*[@alt='Cart']").click()
driver.find_element_by_xpath("//*[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector(".promoCode").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector(".promoInfo").text)'''

#Explicit wait
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
driver.find_element_by_css_selector("button.search-button").click
time.sleep(3)
buttons = driver.find_elements_by_xpath("//div[@class='product-action'] /button")
print(len(buttons))
assert len(buttons) == 3
for button in buttons:
    button.click()
driver.find_element_by_xpath("//*[@alt='Cart']").click()
driver.find_element_by_xpath("//*[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoCode")))
driver.find_element_by_css_selector(".promoCode").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector(".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element_by_css_selector(".promoInfo").text)
