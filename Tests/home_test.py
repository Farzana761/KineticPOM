from selenium import webdriver
from home_page import HomePage  # Import your Page Object classes

# Step 1: Launch the browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Step 2: Create instances of the Page Object classes
home_page = HomePage(driver)

# Step 3: Use the Page Object methods for navigation and verification
home_page.navigate_to("https://automationexercise.com/")
is_home_page_visible = home_page.verify_home_page_text("Home page text is displayed")

if is_home_page_visible:
    print("Home page is visible successfully!")
else:
    print("Home page verification failed")

# Continue with actions on other pages using similar Page Object instances

# Step 4: Close the browser
driver.quit()
