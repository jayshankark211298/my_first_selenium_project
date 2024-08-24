import pytest
from selenium import webdriver
from tc_pim_01 import OrangeHRMTest  # Replace with the actual module name where OrangeHRMTest is defined

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()  # Or any other browser driver
    orange_hrm = OrangeHRMTest(driver)
    yield orange_hrm
    driver.quit()

# Test case to check login functionality with correct credentials (Positive Test)
def test_positive_login(setup):
    setup.login("Admin", "admin123")
    dashboard_element = setup.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(),'Dashboard')]")))
    assert dashboard_element is not None, "ERROR: Login with correct credentials failed."
    print("SUCCESS: Login with correct credentials succeeded.")

# Test case to add a new employee with valid details (Positive Test)
def test_add_employee_positive(setup):
    setup.enter_personal_details("Jay", "shankar.", "k")
    # Verify that the employee was added, for example, by checking if the personal details page is displayed
    personal_details_header = setup.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(),'Personal Details')]")))
    assert personal_details_header is not None, "ERROR: Failed to add a new employee."
    print("SUCCESS: New employee added successfully.")

# Test case to add additional information (Positive Test)
def test_add_additional_information_positive(setup):
    setup.enter_additional_information(
        other_id="12345",
        license_number="20190000998",
        license_expiry="2024-12-31",
        nationality="American",
        marital_status="Single",
        dob="1999-01-31",
        gender="Male"
    )
    # Verify that the additional information was saved, for example, by checking if a success message or the updated details are displayed
    success_message = setup.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-toast-content--success")))
    assert success_message is not None, "ERROR: Failed to add additional information."
    print("SUCCESS: Additional information added successfully.")

# Test case to check login functionality with incorrect credentials (Negative Test)
def test_negative_login(setup):
    setup.login("WrongUser", "WrongPassword")
    error_message = setup.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Invalid credentials')]")))
    assert error_message is not None, "ERROR: Login with incorrect credentials did not fail as expected."
    print("SUCCESS: Login with incorrect credentials failed as expected.")

# Test case to check the addition of employee with missing required details (Negative Test)
def test_add_employee_negative(setup):
    setup.enter_personal_details("", "", "")
    error_message = setup.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Required')]")))
    assert error_message is not None, "ERROR: Missing required details did not trigger an error."
    print("SUCCESS: Error triggered for missing required details as expected.")
