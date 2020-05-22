from selenium.webdriver.common.by import By


class ConfirmPage:

    country_list = (By.ID, "country")

    def __init__(self, driver):
        self.driver = driver

    def get_country(self):
        return self.driver.find_element(*ConfirmPage.country_list)

    choose_country = (By.XPATH, "//div[@class='suggestions']/ul/li/a")

    def send_country(self):
        return self.driver.find_elements(*ConfirmPage.choose_country)

    terms = (By.CSS_SELECTOR, "[for = 'checkbox2']")

    def check_terms(self):
        return self.driver.find_element(*ConfirmPage.terms)

    purhcase = (By.CSS_SELECTOR,"[value='Purchase']")

    def click_purchase(self):
        return self.driver.find_element(*ConfirmPage.purhcase)

    message = (By.XPATH,"//div/strong")

    def confirm_message(self):
        return self.driver.find_element(*ConfirmPage.message)

