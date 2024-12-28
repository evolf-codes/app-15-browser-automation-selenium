# Web Automation with Selenium

This project is a Python-based web automation script using Selenium WebDriver. The script automates logging into the website [DemoQA Login Page](https://demoqa.com/login), filling out a form, and downloading a file. It also includes a configurable download directory for file storage.

## Features

1. **Automated Login**:
   - Navigates to the login page.
   - Inputs username and password.
   - Clicks the login button.

2. **Form Filling**:
   - Automates filling out a form with user details.

3. **File Download**:
   - Automates downloading a file and stores it in a specified directory.

4. **Configurable Download Directory**:
   - Allows setting a default download directory for any files downloaded during the session.

5. **Browser Window Management**:
   - Maximizes the browser window for better visibility during automation.

## Prerequisites

- Python 3.x installed on your system.
- Google Chrome installed.
- ChromeDriver compatible with your Chrome version.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install Dependencies**:
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**:
   - Visit [ChromeDriver](https://chromedriver.chromium.org/downloads) and download the version that matches your Google Chrome version.
   - Place the `chromedriver` executable in the specified directory (e.g., `./chromedriver-mac-arm64/`).

## Usage

1. **Configure the Script**:
   - Ensure the `chromedriver` path is correctly specified in the `Service` setup.
   - Replace the credentials in the `login` method with valid username and password.

2. **Run the Script**:
   ```bash
   python <script_name>.py
   ```

## Code Overview

### Initialization (`__init__` Method)
- Sets up Chrome options, including the default download directory.
- Creates a ChromeDriver instance and maximizes the browser window.

### Login Functionality (`login` Method)
- Opens the DemoQA login page.
- Waits for username, password, and login button elements to become visible.
- Automates entering credentials and logging in.

### Form Filling (`fillForm` Method)
- Navigates to the form page.
- Automates entering details like username, email, current address, and permanent address.

### File Download (`download` Method)
- Navigates to the upload and download section.
- Automates clicking the download button to download a file.

### Cleanup (`quit` Method)
- Closes the browser window and quits the WebDriver instance.

## Example Code

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class WebAutomation:
    def __init__(self):
        chrome_options = Options()
        download_path = os.getcwd()
        prefs = {"download.default_directory": download_path}
        chrome_options.add_experimental_option("prefs", prefs)

        service = Service('./chromedriver-mac-arm64/chromedriver')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.get("https://demoqa.com/login")
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "login")))
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def fillForm(self, username, email, current_address, permanent_address):
        elements_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements_button.click()
        text_box_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box_button.click()
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
        upload_download_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download_button.click()
        download_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "downloadButton")))
        download_button.click()

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    test = WebAutomation()
    test.login(username="testuser", password="Test@1234")
    test.fillForm(username="testuser", email="testuser@email.com", current_address="123 Test St. - current address", permanent_address="123 Test St. - permanent address")
    test.download()
    test.quit()
```

## Notes

- Ensure the ChromeDriver version matches your Chrome browser version.
- The script uses `WebDriverWait` for reliable element interaction.
- Modify the login credentials and form inputs as needed.

## License
This project is open-source and available under the MIT License.


