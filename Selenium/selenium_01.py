#Import the webdriver from selenium
from selenium import webdriver

#Create a driver object and provide the executable file path for the browser
driver = webdriver.Chrome(executable_path="C:\\Python Automation\\Python Training\\chromedriver.exe")

#Maximize the window
driver.maximize_window()

#Open a URL
driver.get("https://www.google.com")

#Get title of the current url
print(driver.title)

#Get the current URL
print(driver.current_url)

#Refresh the current page
driver.refresh()

def url_title():
    print(driver.title)
    print(driver.current_url)

driver.get("https://www.bing.com")
url_title()

#Go back to previos and forward page
driver.back()
url_title()

driver.forward()
url_title()

#Close the current session
driver.close()

#Close all the browser session opened by webdriver
driver.quit()

