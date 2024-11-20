'''
    @Author: Dhananjay Kumar
    @Date: 04-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 04-11-2024
    @Title : Check user valid name
'''

import re
from logger import logger_init  

# Initialize the logger
logger = logger_init("name_validation")

def is_valid_first_name(first_name):
    """
    Check if the first name is valid.

    Parameters:
    first_name (str): The first name to be validated.

    Returns:
    bool: True if the name is valid, False otherwise.
    """
    try:
        # Check if input is a string
        if not isinstance(first_name, str):
            raise ValueError("Input must be a string.")

        # Define the pattern for a valid first name (starts with uppercase, followed by lowercase letters)
        first_name_pattern = r'^[A-Z][a-z]{2,}$'
        is_valid = bool(re.match(first_name_pattern, first_name))

        # Log the validation result
        if is_valid:
            logger.info(f"Valid first name entered: {first_name}")
        else:
            logger.warning(f"Invalid first name entered: {first_name}")

        return is_valid

    except Exception as e:
        logger.error(f"Error occurred while validating name: {e}")
        return False

def main():
    try:
        name = input("Enter your first name: ")
        result = is_valid_first_name(name)  # Check if the entered name is valid
        if result:
            print(f"It is a valid first name: {name}")
        else:
            print(f"It is not a valid first name: {name}")
    except Exception as e:
        logger.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
