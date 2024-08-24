from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class OrangeHRMTest:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")  # Replace with the actual URL of the OrangeHRM site
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        # Find and fill in the username
        username_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        username_input.send_keys(username)

        # Find and fill in the password
        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys(password)

        # Click the login button
        login_button = self.driver.find_element(By.CLASS_NAME, "oxd-button--main")
        login_button.click()

    def enter_personal_details(self, first_name, middle_name, last_name):

        """Add a new employee with provided details, including dropdown selections."""

        add_employee_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add Employee']")))
        add_employee_button.click()

        # Fill in the first name
        first_name_input = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name_input.send_keys(first_name)

        # Fill in the middle name
        middle_name_input = self.driver.find_element(By.NAME, "middleName")
        middle_name_input.send_keys(middle_name)

        # Fill in the last name
        last_name_input = self.driver.find_element(By.NAME, "lastName")
        last_name_input.send_keys(last_name)

        # Click the save button
        save_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        save_button.click()

    def enter_additional_information(self, other_id, license_number, license_expiry, nationality, marital_status, dob, gender):
        # Fill in the Other ID
        other_id_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@class ='oxd-input oxd-input--active'])[3]")))
        other_id_input.send_keys(other_id)

        # Fill in the Driver's License Number
        license_number_input = self.driver.find_element(By.XPATH, "(//input[@class ='oxd-input oxd-input--active'])[4]")
        license_number_input.send_keys(license_number)

        # Fill in the License Expiry Date
        license_expiry_input = self.driver.find_element(By.XPATH, "(//input[@class ='oxd-input oxd-input--active'])[5]")
        license_expiry_input.send_keys(license_expiry)

        # Select Nationality from dropdown
        nationality_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH ,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i")))
        nationality_dropdown.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class ='oxd-select-option'])[83]"))).click()

        # Select Marital Status from dropdown
        marital_status_dropdown = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i")
        marital_status_dropdown.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class ='oxd-select-option'])[2]"))).click()
        # Fill in the Date of Birth
        dob_input = self.driver.find_element(By.XPATH, "(//input[@class ='oxd-input oxd-input--active'])[6]")
        dob_input.send_keys(dob)

        gender_field = self.driver.find_element(By.XPATH, "(//span[@class ='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]")
        gender_field.click()

        # Select Gender
        #if gender.lower() == 'male':
         #  self.driver.find_element(By.ID, "(//span[@class ='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]").click()
        #elif gender.lower() == 'female':
          # self.driver.find_element(By.ID, "(//span[@class ='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]").click()

        # Click the save button
        save_button = self.driver.find_element(By.XPATH, "(//button[@class ='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])[1]")
        save_button.click()

# Example usage
if __name__ == "__main__":
    driver = webdriver.Chrome()  # Or any other browser driver
    test = OrangeHRMTest(driver)

    test.login("Admin", "admin123")
    test.enter_personal_details("Jay", "shankar.", "k")
    test.enter_additional_information(
        other_id="12345",
        license_number="20190000998",
        license_expiry="2024-12-31",
        nationality="American",
        marital_status="India",
        dob="1999-01-31",
        gender="Male"
    )

    driver.quit()