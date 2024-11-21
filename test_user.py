'''
    @Author: Dhananjay Kumar
    @Date: 08-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-11-2024
    @Title : pytest for user registration user valid name, email, and mobile number, and phone no password len 8 charcaters, Should have atleast one uppercase,
    one lowercase, one digit ,has exactly 1 special character.
'''

import pytest
from user import is_valid_first_name, is_valid_last_name, is_valid_email, is_valid_mobile, is_valid_password  # Import functions from employee module

# First name test cases
def test_valid_first_name():
    assert is_valid_first_name("Shaurya") is True  # Valid first name

def test_invalid_first_name():
    assert is_valid_first_name("shaurya") is False  # Starts with lowercase letter
    assert is_valid_first_name("SHAURYA") is False  # All uppercase letters
    assert is_valid_first_name("Sh") is False  # Fewer than 3 characters
    assert is_valid_first_name("S") is False  # Single character
    assert is_valid_first_name("1234") is False  # Starts with digits
    assert is_valid_first_name("!@#") is False  # Special characters only
    assert is_valid_first_name("Shau@") is False  # Special characters at the end

def test_edge_case_names():
    assert is_valid_first_name("S") is False  # Single character should fail
    assert is_valid_first_name("Sha") is True  # Valid 3-letter name

# Last name test cases
def test_valid_last_name():
    assert is_valid_last_name("Kumar") is True  # Valid last name
    assert is_valid_last_name("Smith") is True  # Common valid last name

def test_invalid_last_name():
    assert is_valid_last_name("kumar") is False  # Starts with lowercase
    assert is_valid_last_name("KUMAR") is False  # All uppercase letters
    assert is_valid_last_name("Ku") is False  # Fewer than 3 characters
    assert is_valid_last_name("1234") is False  # Starts with digits
    assert is_valid_last_name("!@#") is False  # Special characters only
    assert is_valid_last_name("Kum@") is False  # Special characters at the end

def test_edge_case_last_names():
    assert is_valid_last_name("K") is False  # Single character name
    assert is_valid_last_name("Kim") is True  # Valid 3-letter last name

# Email test cases
def test_valid_email():
    assert is_valid_email("abc.xyz@bl.co.in") is True  # Valid email with all parts
    assert is_valid_email("abc@bl.co") is True  # Valid email with mandatory parts only

def test_invalid_email():
    assert is_valid_email("abc.xyz@bl.co") is False  # Missing last part
    assert is_valid_email("abc@bl.in") is False  # Missing middle part
    assert is_valid_email("abc@bl") is False  # Missing domain parts after @
    assert is_valid_email("abc@bl.") is False  # Incomplete domain
    assert is_valid_email("abcxyz@bl.co.in") is False  # Missing dot in local part
    assert is_valid_email("abc.@bl.co.in") is False  # Extra dot at the end of local part
    assert is_valid_email("abc..xyz@bl.co.in") is False  # Double dots in local part
    assert is_valid_email("@bl.co.in") is False  # Missing local part
    assert is_valid_email("abc@.co.in") is False  # Missing domain name after @

def test_edge_case_emails():
    assert is_valid_email("a.b@bl.co.in") is True  # Minimal local part with dots
    assert is_valid_email("abc@bl.co.in") is True  # Email without optional middle local part

# Mobile number test cases
def test_valid_mobile():
    assert is_valid_mobile("91 6203494332") is True  # Valid mobile number with country code and space

def test_invalid_mobile():
    assert is_valid_mobile("919919819801") is False  # Missing space after country code
    assert is_valid_mobile("91 991981980") is False  # Less than 10 digits
    assert is_valid_mobile("91 99198198012") is False  # More than 10 digits
    assert is_valid_mobile("92 9919819801") is False  # Incorrect country code
    assert is_valid_mobile("91-9919819801") is False  # Dash instead of space
    assert is_valid_mobile("9919819801") is False  # Missing country code
    assert is_valid_mobile("91 99198A9801") is False  # Contains non-numeric character

def test_edge_case_mobile():
    assert is_valid_mobile("91 0000000000") is True  # Edge case with all zeros, still valid format

# Password test cases
def test_valid_password():
    assert is_valid_password("password123") is True  # Valid password with alphanumeric characters
    assert is_valid_password("Password123!") is True  # Valid password with special characters
    assert is_valid_password("12345678") is True  # Valid password with only digits

def test_invalid_password():
    assert is_valid_password("pass") is False  # Less than 8 characters
    assert is_valid_password("12345") is False  # Less than 8 characters
    assert is_valid_password("1234567") is False  # Less than 8 characters
    assert is_valid_password("password") is False  # Only lowercase letters, no special characters or digits
    assert is_valid_password("PASSWORD123") is False  # Only uppercase letters, no special characters
    assert is_valid_password("!@#$%^&*") is False  # Special characters only, less than 8 characters
    assert is_valid_password("password@") is False  # Only 7 characters, not enough
    assert is_valid_password("short") is False  # Less than 8 characters

def test_edge_case_passwords():
    assert is_valid_password("Shaurya@123") is True  # Password with uppercase, lowercase, digits, and special characters
    assert is_valid_password("a1!b2@c3#") is True  # Complex password with numbers and special characters
    assert is_valid_password("Shaurya123") is True

# Run the test cases
if __name__ == "__main__":
    pytest.main()