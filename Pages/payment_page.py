from selenium.webdriver.common.by import By

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_payment_details(self, name, card_number, cvc, expire_month, expire_year):
        name_element = self.driver.find_element(By.XPATH, "//*[@id='payment-form']/div[1]/div/input")
        name_element.send_keys(name)

        card_element = self.driver.find_element(By.XPATH, "//*[@id='payment-form']/div[2]/div/input")
        card_element.send_keys(card_number)

        cvc_element = self.driver.find_element(By.XPATH, "//*[@id='payment-form']/div[3]/div[1]/input")
        cvc_element.send_keys(cvc)

        expire_month_element = self.driver.find_element(By.XPATH, "//*[@id='payment-form']/div[3]/div[2]/input")
        expire_month_element.send_keys(expire_month)

        expire_year_element = self.driver.find_element(By.XPATH, "//*[@id='payment-form']/div[3]/div[3]/input")
        expire_year_element.send_keys(expire_year)

        place_order_btn = self.driver.find_element(By.XPATH, "//*[@id='submit']")
        place_order_btn.click()
