# cart_page.py
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element(By.XPATH, "//*[@id='cartModal']/div/div/div[3]/button").click()

# Add more methods as needed for interacting with the cart page
