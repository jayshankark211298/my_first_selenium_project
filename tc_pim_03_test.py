from orange_hrm_test import OrangeHRMTest  # Replace with the actual module name where OrangeHRMTest is defined
import pytest

# Set up the initial URL and credentials for testing
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"
password = "admin123"
orange_hrm = OrangeHRMTest(url)

# Test case to check the login functionality with correct credentials (Positive Test)
def test_positive_login():
    orange_hrm.login(url, username, password)
    # Verify that login was successful, for example, by checking the presence of a dashboard element
    dashboard_element = orange_hrm.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(),'Dashboard')]")))
    assert dashboard_element is not None, "ERROR: Login with correct credentials failed."
    print("SUCCESS: Login with correct credentials succeeded.")

# Test case to check login functionality with incorrect credentials (Negative Test)
def test_negative_login():
    orange_hrm.login(url, "WrongUser", "WrongPassword")
    # Verify that login failed, by checking the absence of the dashboard element or presence of an error message
    error_message = orange_hrm.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Invalid credentials')]")))
    assert error_message is not None, "ERROR: Login with incorrect credentials did not fail as expected."
    print("SUCCESS: Login with incorrect credentials failed as expected.")

# Test case to check navigation to Termination Reasons (Positive Test)
def test_navigate_to_termination_reasons():
    orange_hrm.login(url, username, password)
    orange_hrm.navigate_to_termination_reasons()
    # Verify that the Termination Reasons page is displayed
    page_header = orange_hrm.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(),'Termination Reasons')]")))
    assert page_header is not None, "ERROR: Navigation to Termination Reasons failed."
    print("SUCCESS: Navigation to Termination Reasons succeeded.")

# Test case to check the deletion of a termination reason (Positive Test)
def test_delete_termination_reason():
    orange_hrm.login(url, username, password)
    orange_hrm.navigate_to_termination_reasons()
    orange_hrm.delete_termination_reason()
    # Verify that the termination reason has been deleted, for example, by checking for a success message
    success_message = orange_hrm.wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-toast-content--success")))
    assert success_message is not None, "ERROR: Deletion of termination reason failed."
    print("SUCCESS: Deletion of termination reason succeeded.")

# Test case to ensure the browser session is properly closed
def test_closing():
    orange_hrm.close_browser()
    print("SUCCESS: Browser session closed.")
