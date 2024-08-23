from selenium.webdriver.common.by import By

class OrderConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_order_confirmation_message(self, expected_message):
        try:
            success_message_element = self.driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/p")
            actual_message = success_message_element.text

            if expected_message == actual_message:
                return True
            else:
                return False
        except Exception as e:
            print(f"Verification failed: {str(e)}")
            return False

    def continue_after_order_confirmation(self):
        continue_button = self.driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/a")
        continue_button.click()
