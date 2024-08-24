from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os

class OrangeHRM:
    def __init__(self, url):
        self.url = url
        chrome_install = ChromeDriverManager().install()
        folder = os.path.dirname(chrome_install)
        chromedriver_path = os.path.join(folder, "chromedriver.exe")
        self.driver = webdriver.Chrome(service=Service(chromedriver_path))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(self.url)

    def launch_site(self):
        """Launch the OrangeHRM site."""
        self.driver.get(self.url)
        self.driver.maximize_window()

    def login(self, username, password):
        """Login to the OrangeHRM site."""
        username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CLASS_NAME, "oxd-button--main")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def navigate_to_pim(self):
        """Navigate to the PIM module."""
        pim_module = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_module.click()

    def add_employee(self, employee_name, employee_id, employment_status, include_option, supervisor_name, job_title, sub_unit):
        """Add a new employee with provided details, including dropdown selections."""
       # add_employee_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add Employee']")))
        #add_employee_button.click()

        employee_name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")))
        employee_name_field.send_keys(employee_name)

        employee_id_field = self.driver.find_element(By.XPATH, "(//input[@class ='oxd-input oxd-input--active'])[2]")
        employee_id_field.clear()
        employee_id_field.send_keys(employee_id)

        employment_status_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Employment Status']/following-sibling::div//i")))
        employment_status_dropdown.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{employment_status}']"))).click()

        include_dropdown = self.driver.find_element(By.XPATH, "//label[text()='Include']/following-sibling::div//i")
        include_dropdown.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{include_option}']"))).click()

        supervisor_name_field = self.driver.find_element(By.XPATH, "//label[text()='Supervisor Name']/following-sibling::div//input")
        supervisor_name_field.send_keys(supervisor_name)

        job_title_dropdown = self.driver.find_element(By.XPATH, "//label[text()='Job Title']/following-sibling::div//i")
        job_title_dropdown.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{job_title}']"))).click()

        sub_unit_dropdown = self.driver.find_element(By.XPATH, "//label[text()='Sub Unit']/following-sibling::div//i")
        sub_unit_dropdown.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{sub_unit}']"))).click()

        save_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        save_button.click()

        # Optionally click the 'Reset' button if necessary
        # reset_button = self.driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--ghost")
        # reset_button.click()

if __name__ == "__main__":
    # Initialize the OrangeHRM class with the URL of your OrangeHRM site
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    orange_hrm = OrangeHRM(url)

    # Launch the site
    orange_hrm.launch_site()

    # Log in with your username and password
    username = "Admin"
    password = "admin123"
    orange_hrm.login(username, password)

    # Navigate to PIM module
    orange_hrm.navigate_to_pim()

    # Add an employee with the provided details
    employee_name = "Jay shankar k"
    employee_id = "0387"
    employment_status = "Freelance"
    include_option = "Current Employees Only"
    supervisor_name = "suman"
    job_title = "automation"
    sub_unit = "Engineering"

    orange_hrm.add_employee(employee_name, employee_id, employment_status, include_option, supervisor_name, job_title, sub_unit)

    # Close the browser after the test
    orange_hrm.driver.quit()
