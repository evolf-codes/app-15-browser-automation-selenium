from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get("https://demoqa.com/login")
    driver.maximize_window()

    # Locate and fill in the username
    username_field = driver.find_element(By.ID, "userName")
    username_field.send_keys("testuser")  # Replace with your username

    # Locate and fill in the password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Test@1234")  # Replace with your password

    # Click the login button
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    # Wait for a few seconds to observe the results
    time.sleep(5)

    # Check if login was successful
    if "profile" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed.")

finally:
    # Close the browser
    driver.quit()