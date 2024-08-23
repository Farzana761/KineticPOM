from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def verify_homepage(self):
        try:
            text_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='slider-carousel']/div/div[1]/div[1]/h1/span"))
            )
            assert text_element.is_displayed(), "Home page text is displayed"
            print("Home page is visible successfully!")
        except Exception as e:
            print(f"Home page verification failed: {str(e)}")
