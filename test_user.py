'''
    @Author: Dhananjay Kumar
    @Date: 04-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 04-11-2024
    @Title : Pytest for User Registration
'''

import pytest
from user import is_valid_first_name  # Corrected import

def test_valid_first_name():
    assert is_valid_first_name("Shaurya") is True  # Valid first name

def test_invalid_first_name():
    assert is_valid_first_name("shaurya") is False  # Starts with lowercase
    assert is_valid_first_name("SHAURYA") is False  # All uppercase
    assert is_valid_first_name("Sh") is False  # Fewer than 3 characters
    assert is_valid_first_name("1234") is False  # Contains digits
    assert is_valid_first_name("!@#") is False  # Contains special characters
    assert is_valid_first_name("Shau@") is False  # Contains special character at the end

def test_edge_case_names():
    assert is_valid_first_name("S") is False  # Single character
    assert is_valid_first_name("Sha") is True  # Minimum valid name length

# Run the test cases
if __name__ == "__main__":
    pytest.main()
