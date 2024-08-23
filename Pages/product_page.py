# product_page.py
from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button").click()

# Add more methods as needed for interacting with the product page
