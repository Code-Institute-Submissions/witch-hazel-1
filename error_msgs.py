import config

POSITIVE_INT = f"{config.INDENT}Your number must be a positive integer or 0.\
                \n{config.INDENT}Negative and decimal-point numbers, text and special characters, etc. \
                \n{config.INDENT}are not allowed:"

DEFAULT_NOT_A_NUMBER_BLURB = " is not a number. Please enter a number between "
DEFAULT_NOT_IN_RANGE_BLURB = f"{config.INDENT}That number is out of range. Please enter a number between "
NO_START_NUMBER = "The starting number is not recorded."
MORE_THAN_INITIAL = "You ended up with more units than you started with."

def valid_option_number(lower_bound, upper_bound):
    return f"{config.INDENT}Please enter a valid integer between {lower_bound} and {upper_bound}"