import pytest
from selenium.common.exceptions import TimeoutException
from tc_pim_02 import OrangeHRM  # Assuming the class is saved in a file named orange_hrm.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def orange_hrm_instance():
    """Fixture to initialize and close the OrangeHRM instance."""
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    instance = OrangeHRM(url)
    yield instance
    instance.driver.quit()


def test_launch_site(orange_hrm_instance):
    """Test launching the OrangeHRM site."""
    orange_hrm_instance.launch_site()
    assert "OrangeHRM" in orange_hrm_instance.driver.title, "Site launch failed, title mismatch."


def test_login_valid_credentials(orange_hrm_instance):
    """Test login with valid credentials."""
    username = "Admin"
    password = "admin123"
    orange_hrm_instance.login(username, password)
    dashboard_element = orange_hrm_instance.wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
    )
    assert dashboard_element.is_displayed(), "Login failed with valid credentials."


def test_login_invalid_credentials(orange_hrm_instance):
    """Test login with invalid credentials."""
    username = "invalid_user"
    password = "invalid_pass"
    orange_hrm_instance.login(username, password)
    error_message = orange_hrm_instance.wait.until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Invalid credentials')]"))
    )
    assert error_message.is_displayed(), "Error message not displayed for invalid credentials."


def test_navigate_to_pim(orange_hrm_instance):
    """Test navigation to the PIM module."""
    orange_hrm_instance.navigate_to_pim()
    pim_page_element = orange_hrm_instance.wait.until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='PIM']"))
    )
    assert pim_page_element.is_displayed(), "Navigation to PIM module failed."


def test_add_employee(orange_hrm_instance):
    """Test adding a new employee."""
    employee_name = "Jay shankar k"
    employee_id = "0387"
    employment_status = "Freelance"
    include_option = "Current Employees Only"
    supervisor_name = "suman"
    job_title = "automation"
    sub_unit = "Engineering"

    orange_hrm_instance.add_employee(employee_name, employee_id, employment_status, include_option, supervisor_name,
                                     job_title, sub_unit)

    # Verify that the employee was added successfully by searching for the employee
    search_field = orange_hrm_instance.wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
    )
    search_field.send_keys(employee_name)

    search_button = orange_hrm_instance.driver.find_element(By.XPATH, "//button[@type='submit']")
    search_button.click()

    employee_record = orange_hrm_instance.wait.until(
        EC.presence_of_element_located((By.XPATH, f"//div[text()='{employee_name}']"))
    )
    assert employee_record.is_displayed(), "Employee not added successfully."


def test_cleanup(orange_hrm_instance):
    """Close the browser after tests."""
    orange_hrm_instance.driver.quit()
    assert orange_hrm_instance.driver.service.process is None, "Browser was not closed properly."
