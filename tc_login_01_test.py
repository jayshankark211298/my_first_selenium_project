from tc_login_01 import ShankarTestingClass  # Replace with actual module name
import pytest

# Set up the initial URL for testing
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
suman = ShankarTestingClass(url)

# Test case to check if the booting function works correctly (Positive Test)
def test_positive_booting():
    assert suman.booting_function() == True, "ERROR: Booting function did not return True."
    print("SUCCESS: Booting function passed.")

# Test case to check login functionality with correct credentials (Positive Test)
def test_positive_login():
    assert suman.login("Admin", "admin123") == True, "ERROR: Login with correct credentials failed."
    print("SUCCESS: Login with correct credentials succeeded.")

# Test case to check login functionality with incorrect credentials (Negative Test)
def test_negative_login():
    assert suman.login("WrongUser", "WrongPassword") == False, "ERROR: Login with incorrect credentials did not fail as expected."
    print("SUCCESS: Login with incorrect credentials failed as expected.")

# Test case to ensure the browser session is properly closed
def test_closing():
    suman.shutdown()
    print("SUCCESS: Browser session closed.")
