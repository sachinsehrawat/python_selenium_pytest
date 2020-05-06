from selenium import webdriver

#Open Chrome Browser
driver =  webdriver.Chrome(executable_path='C:\Python Automation\Python Training\chromedriver.exe')

#Maximize browser window
driver.maximize_window()

#Open a web page
driver.get('https://rahulshettyacademy.com/angularpractice/')

#find element by id
driver.find_element_by_id('exampleInputPassword1').send_keys('Sachin')

#find element by name]
driver.find_element_by_name('name').send_keys('Sachin')

#find element by class
driver.find_element_by_class_name('form-check-input').click()

#find element by css
#tagname[attribute='value'] -->tagname is optional
driver.find_element_by_css_selector("input[name='email']").send_keys('sachin')

#find element by xpath
#//tagName[@attribute='value']  -->Tag name is optional use * instead
driver.find_element_by_xpath("//input[@type='submit']").click()

#xpath regular expression
#//*[contains(@attribute,value)] --> * can be used in place of tagname
print(driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text)

#xpath parent child traverse
driver.find_element_by_xpath("//div[@class='container']/form/div[1]/input").clear()

driver.get("https://login.salesforce.com/")

#find element by css - regular expression
#tagname[attribute*='value] --> tagname is optional
driver.find_element_by_css_selector("[class*='mt8 username']").send_keys('Sachin')

#find element by css when Id is available
# tagname#id -->tagname is optional
driver.find_element_by_css_selector('#password').send_keys('sachin')

#find element by css when class is available
# tagname.class1.class2.class3 and so on --> tagname is optional
driver.find_element_by_css_selector('.r4.fl.mr8').click()

#find element by link text
#tagname must be 'a' for link text
driver.find_element_by_link_text('Forgot Your Password?').click()

#find element by CSS selector: nth child
driver.find_element_by_css_selector("#forgotPassForm div a:nth-child(4)").click()

driver.close()



