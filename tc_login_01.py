from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class ShankarTestingClass:
    # Initialize the class with the URL and set up the Chrome WebDriver
    def __init__(self, url):
        self.url = url
        chrome_install = ChromeDriverManager().install()

        folder = os.path.dirname(chrome_install)
        chromedriver_path = os.path.join(folder, "chromedriver.exe")
        self.driver = webdriver.Chrome(service=Service(chromedriver_path))
        self.driver.get(self.url)

    def booting_function(self):
        # This function could be used to check the page loading or any other startup actions
        return True

    def login(self, username, password):
        if self.booting_function():
            try:
                # Wait for the username and password fields to be present
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='orangehrm-login-form']//form//input)[2]"))
                )
                # Locate the username and password fields and the login button using XPath
                username_field = self.driver.find_element(By.XPATH,
                                                          "(//div[@class='orangehrm-login-form']//form//input)[2]")
                password_field = self.driver.find_element(By.XPATH,
                                                          "(//div[@class='orangehrm-login-form']//form//input)[3]")
                login_button = self.driver.find_element(By.XPATH,
                                                        "//div[@class='oxd-form-actions orangehrm-login-action']//button")

                # Enter the username and password and click the login button
                username_field.send_keys(username)
                password_field.send_keys(password)
                login_button.click()

                # Wait for the page to load
                time.sleep(5)
                return True
            except Exception as e:
                print(f"ERROR: {e}")
                return False
        else:
            return False

    def shutdown(self):
        self.driver.quit()


if __name__ == "__main__":
    testing_instance = ShankarTestingClass("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    testing_instance.login("Admin", "admin123")
    testing_instance.shutdown()
