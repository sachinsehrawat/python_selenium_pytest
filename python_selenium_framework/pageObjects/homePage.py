from selenium.webdriver.common.by import By


class HomePage:

    shopItem = (By.LINK_TEXT, "Shop")
    #self.driver.find_element_by_link_text("Shop").click()

    def __init__(self, driver):
        self.driver = driver

    def homepageitems(self):
        return self.driver.find_element(*HomePage.shopItem)