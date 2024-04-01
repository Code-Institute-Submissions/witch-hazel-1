"""
Configures colours layouts and prompts.
Because of the prompts, this should be sent to the localiser for translation.
"""

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
COLOR_GREEN = '\u001b[32m'
COLOR_CYAN = '\033[96m'
COLOR_NORMAL = '\033[0m'
COLOR_STRONG_WHITE = '\u001b[37;1m'

INDENT = '  '
SMALL_INDENT = ' '
PROMPT_STRING = f"{SMALL_INDENT}{COLOR_GREEN}Witch-Hazel>>{COLOR_NORMAL} "
MORE_GEN_HELP = f"{INDENT}{COLOR_CYAN}Press Enter to see more general help text ...{COLOR_NORMAL}\n"
BACK_TO_MENU = f"{INDENT}{COLOR_CYAN}Press Enter to go to the main menu ...{COLOR_NORMAL}\n"
EXIT_MSG = f"{INDENT}{COLOR_CYAN}Exiting the Witch-Hazel app ...{COLOR_NORMAL}\n"
LINE_OF_UNDERSCORES = '___________________________________________________________________________'
LINE_OF_POUNDS = '###########################################################################'
