import pytest
from user import is_valid_first_name, is_valid_last_name  # Import functions from user.py

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

# Run the test cases
if __name__ == "__main__":
    pytest.main()