from selenium import webdriver
driver = webdriver.Chrome()
import time
driver.implicitly_wait(5)

# Child - parent traverse
# Check the items searched are correct or not
# Check the items added are available in final card
# Check the discount amount is less than total amount
# Check the total amount is same as sum of items in the cart
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
veg = "ber"
driver.find_element_by_css_selector(".search-keyword").send_keys(veg)
time.sleep(2)
items = driver.find_elements_by_xpath("//*[text()='ADD TO CART']")
list=[]
count = 0
for item in items:
    #1
    list.append((item.find_element_by_xpath("parent::div/parent::div/h4").text))
    #2
    assert veg in list[count]
    count = count +1
    item.click()

driver.find_element_by_xpath("//*[@alt='Cart']").click()
driver.find_element_by_xpath("//*[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
items2 = driver.find_elements_by_css_selector(".product-name")

list2 = []
for item2 in items2:
    list2.append(item2.text)

assert list == list2

