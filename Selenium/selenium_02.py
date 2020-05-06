from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\Python Automation\Python Training\chromedriver.exe')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice')
driver.find_element_by_name('name').send_keys('Sachin S')
driver.find_element_by_id('exampleCheck1').click()
driver.find_element_by_css_selector('input[name="email"]').send_keys('Sachin@mail.com')
