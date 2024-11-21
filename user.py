'''
    @Author: Dhananjay Kumar
    @Date: 08-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-11-2024
    @Title : Check user valid name, email, and mobile number, and phone no.
'''

import re
from logger import logger_init  

# Initialize the logger
logger = logger_init("name_email_mobile_validation")

# Function to validate first name
def is_valid_first_name(first_name):
    try:
        if not isinstance(first_name, str):
            raise ValueError("Input must be a string.")
        first_name_pattern = r'^[A-Z][a-z]{2,}$'
        is_valid = bool(re.match(first_name_pattern, first_name))
        if is_valid:
            logger.info(f"Valid first name entered: {first_name}")
        else:
            logger.warning(f"Invalid first name entered: {first_name}")
        return is_valid
    except Exception as e:
        logger.error(f"Error occurred while validating first name '{first_name}': {e}")
        return False

# Function to validate last name
def is_valid_last_name(last_name):
    try:
        if not isinstance(last_name, str):
            raise ValueError("Input must be a string.")
        last_name_pattern = r'^[A-Z][a-z]{2,}$'
        is_valid = bool(re.match(last_name_pattern, last_name))
        if is_valid:
            logger.info(f"Valid last name entered: {last_name}")
        else:
            logger.warning(f"Invalid last name entered: {last_name}")
        return is_valid
    except Exception as e:
        logger.error(f"Error occurred while validating last name '{last_name}': {e}")
        return False

# Function to validate email
def is_valid_email(email):
    try:
        if not isinstance(email, str):
            raise ValueError("Input must be a string.")
        email_pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$'
        is_valid = bool(re.match(email_pattern, email))
        if is_valid:
            logger.info(f"Valid email entered: {email}")
        else:
            logger.warning(f"Invalid email entered: {email}")
        return is_valid
    except Exception as e:
        logger.error(f"Error occurred while validating email '{email}': {e}")
        return False

# Function to validate mobile number
def is_valid_mobile(mobile):
    try:
        if not isinstance(mobile, str):
            raise ValueError("Input must be a string.")
        mobile_pattern = r'^91\s\d{10}$'
        is_valid = bool(re.match(mobile_pattern, mobile))
        if is_valid:
            logger.info(f"Valid mobile number entered: {mobile}")
        else:
            logger.warning(f"Invalid mobile number entered: {mobile}")
        return is_valid
    except Exception as e:
        logger.error(f"Error occurred while validating mobile number '{mobile}': {e}")
        return False

# Function to validate password
def is_valid_password(password):
    """
    Check if the password is valid.

    Parameters:
    password (str): The password to be validated.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
    try:
        if not isinstance(password, str):
            raise ValueError("Input must be a string.")
        
        # Password pattern: Minimum 8 characters
        password_pattern = r'^[A-Za-z0-9!@#$%^&*()_+]{8,}$'
        is_valid = bool(re.match(password_pattern, password))
        
        if is_valid:
            logger.info(f"Valid password entered.")
        else:
            logger.warning(f"Invalid password entered: {password}")

        return is_valid
    except Exception as e:
        logger.error(f"Error occurred while validating password: {e}")
        return False

def main():
    try:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        mobile = input("Enter your mobile number (format: '91 9919819801'): ")
        password = input("Enter your password (minimum 8 characters): ")

        # Validate first name, last name, email, mobile number, and password
        first_name_valid = is_valid_first_name(first_name)
        last_name_valid = is_valid_last_name(last_name)
        email_valid = is_valid_email(email)
        mobile_valid = is_valid_mobile(mobile)
        password_valid = is_valid_password(password)

        if first_name_valid and last_name_valid and email_valid and mobile_valid and password_valid:
            print(f"All entries are valid: {first_name} {last_name}, {email}, {mobile}, Password is valid")
        else:
            if not first_name_valid:
                print(f"Invalid first name: {first_name}")
            if not last_name_valid:
                print(f"Invalid last name: {last_name}")
            if not email_valid:
                print(f"Invalid email: {email}")
            if not mobile_valid:
                print(f"Invalid mobile number: {mobile}")
            if not password_valid:
                print(f"Invalid password: {password}")

    except Exception as e:
        logger.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()