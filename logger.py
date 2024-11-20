'''
    @Author: Dhananjay Kumar
    @Date: 04-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 04-11-2024
    @Title : Logger file containing logger function

'''

import logging

def logger_init(name, log_file='all.log', level=logging.INFO):
    """
    Initialize and return a logger that logs to both a file and the console.

    Parameters:
    name (str): The name of the logger (usually the module name).
    log_file (str): The file to which the log messages will be saved.
    level (int): The logging level (default is logging.INFO).

    Returns:
    logger: The configured logger.
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)  # Set the log level for the logger

    # Define the formatter for log messages
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

    # File handler for writing logs to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)  

    # Stream handler for printing logs to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)  

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

# Example usage:
if __name__ == "__main__":
    logger = logger_init("example")

    # Log messages with different severity levels
    logger.debug("This is a debug message")  
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")