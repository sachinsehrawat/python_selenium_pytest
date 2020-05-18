from selenium import webdriver
driver = webdriver.Chrome()
import time
driver.implicitly_wait(5)

#1 Child - parent traverse
#2 Check the items searched are correct or not
#3 Check the items added are available in final card
#4 Check the discount amount is less than total amount
#5 Check the total amount is same as sum of items in the cart
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
#3
assert list == list2

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
code = driver.find_element_by_class_name("promoInfo").text

total_amount = driver.find_element_by_css_selector(".totAmt").text
after_discount = driver.find_element_by_css_selector(".discountAmt").text
#4
assert int(total_amount) >  float(after_discount)

#5
amount = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amt in amount:
    sum = sum + int(amt.text)
assert sum == int(total_amount)
