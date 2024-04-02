"""
Well ... error messages
"""

import config

POSITIVE_INT = f"{config.INDENT}Your number must be a positive integer or 0.\
    \n{config.INDENT}Negative and decimal-point numbers, text and special characters, etc. \
    \n{config.INDENT}are not allowed. \
    \n\n{config.PROMPT_STRING}"

DEFAULT_NOT_A_NUMBER_BLURB = " is not an integer. Please enter an integer between "
DEFAULT_NOT_IN_RANGE_BLURB = f"{config.INDENT}That number is out of range. \
Please enter a number between "
DEFAULT_NOT_A_YN_ANS_BLURB = f" is not a 'y' or a 'n'. Please enter either a 'y' or a 'n'.\
    \n\n{config.PROMPT_STRING}"
NO_START_NUMBER = "The starting number is not recorded."
MORE_THAN_INITIAL = "You ended up with more units than you started with."
YEAR_NOT_FINISHED = f"{config.INDENT}All seasonal operations for the current year\
    have not been completed.\
    \n{config.INDENT}Check the seasonal jobs and complete them before starting a new year!\
    \n\n{config.PROMPT_STRING}"

def valid_option_number(lower_bound, upper_bound):
    return f"{config.INDENT}Please enter a valid integer between {lower_bound} and {upper_bound}.\
        \n\n{config.PROMPT_STRING}"

def detailed_help_not_int(user_input, mini, maxi):
    return f"{config.INDENT}'{user_input}' is not an integer within the correct range! For detailed\
    \n{config.INDENT}help, type a string of the form 'help [n], where '[n]' represents a valid\
    \n{config.INDENT}integer between {mini} and {maxi}!\
    \n\n{config.PROMPT_STRING}"

def too_many_grafts_planned(planned, available):
    return f"{config.INDENT}You can't plan more grafts than you have rootstocks available!\
    \n{config.INDENT}You have planned {planned} grafts, but you only have {available} rootstocks \
available."

def too_many_grafts_made(made, available):
    return f"{config.INDENT}You can't have made more grafts than you had rootstocks \
available!\
    \n{config.INDENT}You're recording {made} grafts, but you only had {available} rootstocks \
available.\
    \n{config.INDENT}ou first need to record the extra rootstocks you required to create them!"

def too_many_rootstocks_lost(total):
    return f"{config.INDENT}You can't have lost more rootstocks than you actually had in the \
    nursery!\
        \n{config.INDENT}Please enter an integer between 0 and {total}. \
        \n\n{config.PROMPT_STRING}"

def too_many_plants_lost(total):
    return f"{config.INDENT}You can't have lost more plants of this category than you actually\
        \n{config.INDENT}had in the nursery!\
        \n{config.INDENT}Please enter an integer between 0 and {total}. \
        \n\n{config.PROMPT_STRING}"

def too_many_plants_held(number_from):
    return f"{config.INDENT}You can't hold back more plants of this category than you actually\
        \n{config.INDENT}have in the nursery! Please enter an integer between 0 and {number_from}. \
        \n\n{config.PROMPT_STRING}"

def too_many_plants_brought(number_from):
    return f"{config.INDENT}You can't bring forward more plants of this category than you actually\
        \n{config.INDENT}have in the nursery!\
        \n{config.INDENT}Please enter an integer between 0 and {number_from}. \
    \n\n{config.PROMPT_STRING}"

def a_and_b(a, b):
    return f"{a} and {b}. \
    \n\n{config.PROMPT_STRING}"
