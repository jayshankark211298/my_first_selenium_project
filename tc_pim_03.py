from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


class OrangeHRMTest:
    def __init__(self, url):
        self.url = url
        chromedriver_path = r'C:\Users\User\Desktop\workspace\PAT-25\Jay_selenium\chromedriver.exe'  # Replace with your actual path
        self.driver = webdriver.Chrome(service=Service(chromedriver_path))
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait with a 10-second timeout

    def login(self, url, username, password):
        self.driver.get(url)
        self.driver.maximize_window()

        # Find and fill the username
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))).send_keys(username)
        # Find and fill the password
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        # Click the login button
        self.driver.find_element(By.CLASS_NAME, "oxd-button--main").click()

    def navigate_to_termination_reasons(self):
            # Go to PIM module
            pim_module = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "(//a[@class ='oxd-main-menu-item'])[2]")))
            pim_module.click()

            # Wait for the configuration dropdown to be visible and hover over it
            config_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Configuration')]")))
            config_dropdown.click()
            # Click on 'Termination Reasons'
            termination_reason = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[5]")))
            termination_reason.click()

    def delete_termination_reason(self):
        # Select the checkbox of the termination reason to be deleted
        checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[3]/div/button[1]/i")))
        checkbox.click()



        # Confirm the deletion in the modal
        confirm_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button--label-danger.orangehrm-button-margin")))
        confirm_button.click()

    def close_browser(self):
        self.driver.quit()


if __name__ == "__main__":
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'  # Replace with the actual URL
    username = 'Admin'  # Replace with actual username
    password = 'admin123'  # Replace with actual password

    # Instantiate the OrangeHRMTest class
    orange_hrm = OrangeHRMTest(url)

    orange_hrm.login(url, username, password)
    orange_hrm.navigate_to_termination_reasons()
    orange_hrm.delete_termination_reason()
    orange_hrm.close_browser()
