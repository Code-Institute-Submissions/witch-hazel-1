import config
import input_texts

#Main menu messages

PLAN_GRAFTS = "You've chosen to plan your grafting campaign."  # OPTION 1
TAKE_GRAFTS = "You've chosen to record a number of new grafts." # OPTION 2
POT_UP_CUTTINGS = "You've chosen to record potting up some rooted cuttings." # etc.
PLAN_CUTTINGS = "You've chosen to plan this year's cutting campaign."
TAKE_CUTTINGS = "You've chosen to record having taken some cuttings."
RECORD_LOSS = "You've chosen to record the loss of a number of plants."
RECORD_ACQ = "You've chosen to record the acquisition of a number of plants."
HOLD_BACK = "You've chosen to hold a number of grafted plants back a year."
BRING_FORWARD = "You've chosen to bring a number of grafted plants forward a year."
NEW_YEAR = "You've chose to close out the year and open a new year."  # OPTION 0

EXIT_MSG = "Exiting the Witch-Hazel app ..."
ANY_KEY_MSG = "Press Enter to continue ..."
MORE_GEN_HELP = "Press Enter to see more general help text"
SPECIFIC_HELP_PROMPT = f"{config.INDENT}For help on a particular option in the app, please type 'help'\
        \n{config.INDENT}followed by a space, followed by the number of the option for which you\
        \n{config.INDENT}want help (e.g. 'help 6' for help on Option 6)."

CUTTINGS_LATER = "You've chosen to plan your cutting campaign later!"

TAKE_MORE_CUTTINGS = f"{config.INDENT}Would you like to add additional cuttings taken now?\
        \n{input_texts.Y_OR_N_TEXT} \n"

CANCEL_TAKE_CUTTINGS = f"{config.INDENT}Cuttings taken action cancelled.\
        \n{config.INDENT}No changes have been made to the data."

REOPENING = f"{config.INDENT}Reopening ..."

BACK_TO_MENU = f"{config.INDENT}Press Enter to go back to the main menu ..."

CUTTINGS_SUCCESSFUL = f"{config.INDENT}Cuttings campaign record added successfully."

TAKE_CUTTINGS_NOW = f"{config.INDENT}Would you like enter some cuttings taken now?\
            \n{input_texts.Y_OR_N_TEXT} \n"

WHICH_CULTIVAR_P = f"{config.INDENT}For which cultivar would you like to plan your grafting campaign?\
    \n"
WHICH_CULTIVAR_M = f"{config.INDENT}For which cultivar would you like record new grafts made?\
    \n"


NO_GRAFTS_YET_TAKEN = f"{config.INDENT}You have not yet planned to make any grafts of this cultivar.\
            \n{config.INDENT}Would you like to do so now?\
            \n{input_texts.Y_OR_N_TEXT} \n"

def main_menu_prompt(lower_bound, upper_bound):
    return f"{config.INDENT}Please choose an option by entering its number (between {lower_bound} and {upper_bound}):\
        \n{config.INDENT}Type 'HELP' or 'HELP [n]' for help (where [n] indicates the number on which\
        \n{config.INDENT}you want detailed help), or 'EXIT' to quit:\n"

def a_and_b(a, b):
    return f"{a} and {b}"

def a_out_of_b(a, b):
    return f"{a} out of {b}"

def task_completed(string):
    return f"{config.INDENT}You have completed the '{string}' task for the year!\
        \n{config.INDENT}You can still reopen the task if you wish to make any changes until you close out the year.\
        \n"

def task_not_completed(string):
    return f"{config.INDENT}You have not yet completed the task '{string}' for the year.\
        \n{config.INDENT}You can come by later and modify the current figure."

def detailed_help_choice(string):
    return f"You have chosen help on Option {string}."


def planned_cuttings_taken(taken, planned):
    return f"{config.INDENT} You have already reached the number of cuttings you planned to take this year: \
        \n{config.INDENT}{taken} cuttings taken out of {planned} planned!"

def cuttings_taken(taken, planned):
    return f"{config.INDENT}So far you have taken {taken} cuttings this year!\
        \n{config.INDENT}You have planned to take a total of {planned} cuttings for this year."

def no_cuttings_yet_taken(planned):
    return f"{config.INDENT}You have not yet taken any cuttings this year!\
            \n{config.INDENT}You have planned to take a total of {planned} cuttings for this year."

def task_closed_reopen(task):
    return f"\n{config.INDENT}The task '{task}' has been closed for the year.\
        \n{config.INDENT}Would you like to reopen it?\
        \n{input_texts.Y_OR_N_TEXT}\n"

def do_not_reopen(task):
    return f"{config.INDENT}You have decided not to re-open the '{task}' task, which has been closed for this year\
            \n{config.INDENT}No changes have been made to your data."

def planned_cuttings_reached(planned, taken):
    return f"{config.INDENT}Congratulations! You have achieved the planned number of cuttings: \
            \n{config.INDENT}{taken} cuttings taken out of {planned} planned!"

def planned_cuttings_not_reached(planned, taken):
    return f"{config.INDENT}You have now taken a total of {taken} cuttings out of a planned total\
            \n{config.INDENT}of {planned}!"

def plan_for(cultivar):
    return f"plan grafts for {cultivar}"

def planned_for(cultivar):
    return f"{config.INDENT}You have chosen to plan graft numbers for {current_cultivar}."

def rootstocks_unplanned():
    return f"{config.INDENT}You have a total of {stock} rootstocks in stock, of which {unreserved} have not yet\
        \n{config.INDENT}been reserved in planning for other cultivars.\
        \n"

def replace_value(old_value):
    return f"{config.INDENT}So far, you have planned to make {old_value} grafts of this cultivar.\
            \n{config.INDENT}Would you like to replace this value? "

def planned_grafts_changed(cultivar, new_value):
    return f"{config.INDENT}Planned number of grafts for {cultivar} successfully changed to {new_value}."

def task_cancelled(task, cultivar):
    return f"{config.INDENT}This {task_string} action for {current_cultivar} has been cancelled.\
            \n{config.INDENT}No changes have been made to the data."

















def year_created(year, cuttings):
    return f"{config.INDENT}Year {year} created. {cuttings} cuttings planned\
        \n{config.INDENT}for this year."

