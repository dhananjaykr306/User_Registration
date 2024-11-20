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

def is_valid_first_name(first_name):
    """
    Check if the first name is valid.

    Parameters:
    first_name (str): The first name to be validated.

    Returns:
    bool: True if the name is valid, False otherwise.
    """
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
        logger.error(f"Error occurred while validating first name: {e}")
        return False

def is_valid_last_name(last_name):
    """
    Check if the last name is valid.

    Parameters:
    last_name (str): The last name to be validated.

    Returns:
    bool: True if the name is valid, False otherwise.
    """
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
        logger.error(f"Error occurred while validating last name: {e}")
        return False

def is_valid_email(email):
    """
    Check if the email is valid based on the specified format.

    Parameters:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    try:
        if not isinstance(email, str):
            raise ValueError("Input must be a string.")

        # Email pattern with mandatory and optional parts
        email_pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$'
        is_valid = bool(re.match(email_pattern, email))

        if is_valid:
            logger.info(f"Valid email entered: {email}")
        else:
            logger.warning(f"Invalid email entered: {email}")

        return is_valid

    except Exception as e:
        logger.error(f"Error occurred while validating email: {e}")
        return False

def is_valid_mobile(mobile):
    """
    Check if the mobile number is valid based on the specified format (e.g., "91 9919819801").

    Parameters:
    mobile (str): The mobile number to be validated.

    Returns:
    bool: True if the mobile number is valid, False otherwise.
    """
    try:
        if not isinstance(mobile, str):
            raise ValueError("Input must be a string.")

        # Mobile number pattern: country code followed by a space and a 10-digit number
        mobile_pattern = r'^91\s\d{10}$'
        is_valid = bool(re.match(mobile_pattern, mobile))

        if is_valid:
            logger.info(f"Valid mobile number entered: {mobile}")
        else:
            logger.warning(f"Invalid mobile number entered: {mobile}")

        return is_valid

    except Exception as e:
        logger.error(f"Error occurred while validating mobile number: {e}")
        return False

def main():
    try:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        mobile = input("Enter your mobile number (format: '91 9919819801'): ")

        # Validate first name, last name, email, and mobile number
        first_name_valid = is_valid_first_name(first_name)
        last_name_valid = is_valid_last_name(last_name)
        email_valid = is_valid_email(email)
        mobile_valid = is_valid_mobile(mobile)

        if first_name_valid and last_name_valid and email_valid and mobile_valid:
            print(f"All entries are valid: {first_name} {last_name}, {email}, {mobile}")
        else:
            if not first_name_valid:
                print(f"Invalid first name: {first_name}")
            if not last_name_valid:
                print(f"Invalid last name: {last_name}")
            if not email_valid:
                print(f"Invalid email: {email}")
            if not mobile_valid:
                print(f"Invalid mobile number: {mobile}")

    except Exception as e:
        logger.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()