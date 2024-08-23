# checkout_page.py
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def register_login(self):
        self.driver.find_element(By.XPATH, "//*[@id='do_action']/div[1]/div/div/a").click()

# Add more methods as needed for interacting with the checkout page
