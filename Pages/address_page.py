from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddressPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_address_form(self, first_name, email, password, day, month, year, description):
        mrs_radio_button = self.driver.find_element(By.XPATH, "//*[@id='id_gender2']")
        mrs_radio_button.click()

        password_element = self.driver.find_element(By.XPATH, "//*[@id='password']")
        password_element.send_keys(password)

        day_dropdown = Select(self.driver.find_element(By.XPATH, "//*[@id='days']"))
        day_dropdown.select_by_value(day)

        month_dropdown = Select(self.driver.find_element(By.XPATH, "//*[@id='months']"))
        month_dropdown.select_by_visible_text(month)

        year_dropdown = Select(self.driver.find_element(By.XPATH, "//*[@id='years']"))
        year_dropdown.select_by_visible_text(year)

        description_element = self.driver.find_element(By.XPATH, "//*[@id='ordermsg']/textarea")
        description_element.send_keys(description)

        continue_button = self.driver.find_element(By.XPATH, "//*[@id='cart_items']/div/div[7]/a")
        continue_button.click()
