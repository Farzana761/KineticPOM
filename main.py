from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Initialize the page objects
home_page = HomePage(driver)
product_details_page = ProductPage(driver)
view_cart_page = CartPage(driver)

# Automation flow
try:
    home_page.verify_homepage()

    # Your automation flow continues here
    # ...

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    driver.quit()