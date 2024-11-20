'''
    @Author: Dhananjay Kumar
    @Date: 04-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 04-11-2024
    @Title : Check user valid name, email 
'''

import re
from logger import logger_init  

# Initialize the logger
logger = logger_init("name_email_validation")

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
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def main():
    try:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")

        # Validate first name, last name, and email
        first_name_valid = is_valid_first_name(first_name)
        last_name_valid = is_valid_last_name(last_name)
        email_valid = is_valid_email(email)

        if first_name_valid and last_name_valid and email_valid:
            print(f"All entries are valid: {first_name} {last_name}, {email}")
        else:
            if not first_name_valid:
                print(f"Invalid first name: {first_name}")
            if not last_name_valid:
                print(f"Invalid last name: {last_name}")
            if not email_valid:
                print(f"Invalid email: {email}")

    except Exception as e:
        logger.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()