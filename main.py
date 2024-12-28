import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebAutomation:
    def __init__(self):
        # set options
        chrome_options = Options()
        download_path = os.getcwd()
        prefs = {
            "download.default_directory": download_path,  # Set the default download directory
        }
        chrome_options.add_experimental_option("prefs", prefs)

        # define service
        service = Service('./chromedriver-mac-arm64/chromedriver')

        # define driver
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.get("https://demoqa.com/login")

        # Locate username, password and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "login")))

        # Fill in username, password and login
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def fillForm(self, username, email, current_address, permanent_address):
        # Locate the Elements dropdown and Text Box
        elements_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements_button.click()

        # Locate the form fields
        text_box_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box_button.click()

        # Fill in the form fields
        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        full_name_field.send_keys(username)

        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        email_field.send_keys(email)

        current_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        current_address_field.send_keys(current_address)

        permanent_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        permanent_address_field.send_keys(permanent_address)

        submit_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "submit")))
        submit_button.click()

    def download(self):
        # locate updload and download section and locatate the button
        upload_download_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download_button.click()

        download_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "downloadButton")))
        download_button.click()

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    test = WebAutomation()

    test.login(username="testuser",
               password="Test@1234")

    test.fillForm(username="testuser",
                  email="testuser@email.com",
                  current_address="123 Test St. - current address",
                  permanent_address="123 Test St. - permanent address")

    test.download()

    test.quit()