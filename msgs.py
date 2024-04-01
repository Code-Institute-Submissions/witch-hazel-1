"""
This where the main texts (other than help texts) shown to
provide information to the user are stored.
"""

import config

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
NEW_YEAR = "You've chosen to close out the year and open a new year."  # OPTION 0

SPECIFIC_HELP_PROMPT = f"{config.INDENT}For help on a particular option in the app,\
please type 'help'\
        \n{config.INDENT}followed by a space, followed by the number of the option for which you\
        \n{config.INDENT}want help (e.g. 'help 6' for help on Option 6)."

CUTTINGS_LATER = "You've chosen to plan your cutting campaign later!"

CUTTINGS_CANCELLED = f"{config.INDENT}Cuttings taken action cancelled.\
        \n{config.INDENT}No changes have been made to the data."

REOPENING = f"{config.INDENT}Reopening ..."

CUTTINGS_SUCCESSFUL = f"{config.INDENT}Cuttings campaign record added successfully."

WHICH_CULTIVAR_P = f"{config.INDENT}For which cultivar would you like to plan your\
grafting campaign?\
    \n"
WHICH_CULTIVAR_M = f"{config.INDENT}For which cultivar would you like record new grafts made?\
    \n"

PLAN_CUTTINGS = "planning cuttings"

POT_ROOTED = "potting rooted cuttings"

PLANNED_CUTTINGS_CHANGED = f"{config.INDENT}Number of cuttings planned for this year \
successfully changed."

POTTING_CANCELLED = f"{config.INDENT}Record new cuttings potted action cancelled.\
            \n{config.INDENT}No changes have been made to the data."

NEW = "new "

IN_ADDITION = f" in addition to the ones\
            \n{config.INDENT}you have already recorded"

PLAN_CUTTINGS_CANCELLED = f"{config.INDENT}Plan cuttings action cancelled.\
        \nNo changes have been made to the data."

TAKING_CUTTINGS = 'record cuttings taken'

ADDED_CUTTINGS = f"{config.INDENT}Successfully added to the number of cuttings taken so \
far in this campaign."

LOST_WHICH_CULTIVAR = f"{config.INDENT}For which cultivar would you like record a loss?"

LOSS_RECORDED = f"{config.INDENT}Loss recorded successfully."

GAINED_WHICH_CULTIVAR = f"{config.INDENT}For which cultivar would you like record an acquisition?"

GAIN_RECORDED = f"{config.INDENT}Acquisition recorded successfully."

HOLD_WHICH_CULTIVAR = f"{config.INDENT}For which cultivar would you like hold back plants?"

NO_HOLD_YEAR_ONE = f"{config.INDENT}Year-one plants cannot be held back. Enter 2 or higher. But\
        \n{config.INDENT}there's no point in entering an age greater than the age of the nursery."

ENTER_HOLD_YEAR = f"{config.INDENT}Please enter an integer between 2 and the age of the nursery."

HOLD_RECORDED = f"{config.INDENT}Plants held back successfully."

BRING_WHICH_CULTIVAR = f"{config.INDENT}For which cultivar would you like bring plants forward?"

ENTER_BRING_YEAR = f"{config.INDENT}Please enter an integer between 1 and the age of the nursery."

BRING_RECORDED = f"{config.INDENT}Plants brought forward successfully."

def list_of_options(color=config.COLOR_NORMAL):
    return  f"{config.INDENT}{config.INDENT}{config.COLOR_STRONG_WHITE}1. Plan grafts for this year\
        \n{config.INDENT}{config.INDENT}2. Record grafts taken\
        \n{config.INDENT}{config.INDENT}3. Record rooted cuttings potted up\
        \n{config.INDENT}{config.INDENT}4. Plan this year's cutting campaign\
        \n{config.INDENT}{config.INDENT}5. Record cuttings taken\
        \n\n{config.INDENT}{config.INDENT}6. Record plant losses\
        \n{config.INDENT}{config.INDENT}7. Record plant gains\
        \n{config.INDENT}{config.INDENT}8. Hold grafted plants over for one year\
        \n{config.INDENT}{config.INDENT}9. Bring grafted plants forward one year\
{config.COLOR_NORMAL}\
        \n\n{config.INDENT}{config.INDENT}{color}0. Close out current year{config.COLOR_NORMAL}\
        \n"


def main_menu_prompt(lower_bound, upper_bound):
    return f"{config.INDENT}Please choose an option by entering its number (between {lower_bound} \
and {upper_bound}).\
        \n{config.INDENT}Disabled options will be displayed in a weaker colour than the \
{config.COLOR_STRONG_WHITE}enabled{config.COLOR_NORMAL}\
        \n{config.INDENT}options.\
        \n{config.INDENT}Type 'HELP' or 'HELP [n]' for help (where [n] indicates the number\
        \n{config.INDENT}on which you want detailed help), or 'EXIT' to quit.\
        \n{config.PROMPT_STRING}"

def a_out_of_b(a, b):
    return f"{config.INDENT}{a} out of {b}"

def task_completed(string):
    return f"{config.INDENT}You have completed the task\
        \n{config.INDENT}'{string}' for the year!\
        \n{config.INDENT}You can still reopen the task if you wish to make any changes until\
        \n{config.INDENT}you close out the year.\
        \n"

def task_not_completed(string):
    return f"{config.INDENT}You have not yet completed the task '{string}' for the year.\
        \n{config.INDENT}You can come by later and modify the current figure."

def detailed_help_choice(string):
    return f"You have chosen help on Option {string}."


def planned_cuttings_taken(taken, planned):
    return f"{config.INDENT} You have already reached the number of cuttings you planned to take \
this year:\
        \n{config.INDENT}{taken} cuttings taken out of {planned} planned!"

def cuttings_taken(taken, planned):
    return f"{config.INDENT}So far you have taken {taken} cuttings this year!\
        \n{config.INDENT}You have planned to take a total of {planned} cuttings for this year."

def no_cuttings_yet_taken(planned):
    return f"{config.INDENT}You have not yet taken any cuttings this year!\
            \n{config.INDENT}You have planned to take a total of {planned} cuttings for this year."

def do_not_reopen(task):
    return f"{config.INDENT}You have decided not to re-open the \
    \n{config.INDENT}'{task}' task,\
    \n{config.INDENT}which has been closed for this year\
            \n{config.INDENT}No changes have been made to your data."

def planned_cuttings_reached(planned, taken):
    return f"{config.INDENT}Congratulations! You have achieved the planned number of cuttings: \
            \n{config.INDENT}{taken} cuttings taken out of {planned} planned!"

def planned_cuttings_not_reached(planned, taken):
    return f"{config.INDENT}You have now taken a total of {taken} cuttings out of a planned total\
            \n{config.INDENT}of {planned}!"

def plan_for(cultivar):
    return f"plan grafts for {cultivar}"

def make_grafts(cultivar):
    return f"make grafts for {cultivar}"

def grafts_cancelled(cultivar):
    return f"{config.INDENT}Plan grafts action for {cultivar} cancelled.\
            \n{config.INDENT}No changes have been made to the data."

def planned_for(cultivar):
    return f"{config.INDENT}You have chosen to plan graft numbers for {cultivar}."

def rootstocks_unplanned(stock, unreserved):
    return f"{config.INDENT}You have a total of {stock} rootstocks in stock, of which {unreserved}\
        \n{config.INDENT}have not yet been reserved in planning for other cultivars.\
        \n"

def planned_grafts_changed(cultivar, new_value):
    return f"{config.INDENT}Planned number of grafts for {cultivar} \
    \n{config.INDENT}successfully changed to {new_value}."

def task_cancelled(task, cultivar):
    return f"{config.INDENT}This {task} action for {cultivar}\
        \n{config.INDENT}has been cancelled.\
        \n{config.INDENT}No changes have been made to the data."

def cultivar_chosen(cultivar):
    return f"{config.INDENT}You have chosen to record grafts of {cultivar}"

def cultivar_grafts_planned(number):
    return f"{config.INDENT}You have planned to make {number} of this cultivar."

def grafts_successfully_made(cultivar, grafts, planned):
    return f"{config.INDENT}Number of grafts made for {cultivar}\
        \n{config.INDENT}successfully changed.\
        \n{config.INDENT}The new total of grafts made this year for this cultivar is {grafts}.\
        \n{config.INDENT}You originally planned to make {planned}.\
        \n{config.INDENT}Successfully completed record of new grafts made."

def planned_cuttings(planned):
    return f"\n{config.INDENT}The present planned figure for this year is {planned}."


def more_potted_than_taken(newly_potted, rootstocks, taken):
    return f"{config.INDENT}If {newly_potted} is added to the existing figure of\
        \n{config.INDENT}newly rooted cuttings ({rootstocks}), then you'll have potted up\
        \n{config.INDENT}more cuttings than you took in the Autumn ({taken}).\
        \n{config.INDENT}That is not possible. The absolute maximum number you can pot up in this\
        \n{config.INDENT}session is {taken - newly_potted}.\
        \n{config.INDENT}Action cancelled. No changes have been made to the data."


def potted_up(potted, taken):
    return f"{config.INDENT}You have now potted up {potted} cuttings out of a total of {taken}\
        \n{config.INDENT}(minus any that have failed to root)!\
        \n{config.INDENT}You will use them as rootstocks during the grafting campaign\
        \n{config.INDENT}next season (once they have established themselves in their pots)."

def total_rootstocks(total):
    return f"{config.INDENT}At the last count there were {total} new rootstocks in the nursery."

def rootstock_loss_recorded(number, total):
    return f"{config.INDENT}Loss of {number} new rootstocks recorded.\
        \n{config.INDENT}You now have a stock of {total} new rootstocks."

def loss_chosen(cultivar, year, remaining):
    return f"{config.INDENT}You have chosen to record a loss of {cultivar}\
        \n{config.INDENT}of age Year-{year}.\
        \n{config.INDENT}There are currently {remaining} plants of that category recorded in\
        \n{config.INDENT}the system."

def plants_lost_recorded(lost, cultivar, year, remaining):
    return f"{config.INDENT}Loss of {lost} {cultivar} of Year-{year} recorded.\
    \n{config.INDENT}You now have a remaining stock of {remaining} plants of that category."

def rootstock_gain_recorded(number, total):
    return f"{config.INDENT}Acquisition of {number} new rootstocks recorded.\
        \n{config.INDENT}You now have a stock of {total}\
        \n{config.INDENT}new rootstocks."

def gain_chosen(cultivar, year, total):
    return f"{config.INDENT}You have chosen to register an acquisition of {cultivar}\
        \n{config.INDENT}of age year-{year}.\
        \n{config.INDENT}There are currently {total} plants of that category recorded\
        \n{config.INDENT}in the system."

def plants_gain_recorded(number, cultivar, year, total):
    return f"{config.INDENT}Acquisition of {number} {cultivar}\
        \n{config.INDENT}of Year-{year} recorded.\
        \n{config.INDENT}You currently have a stock of {total} plants of that category."

def hold_chosen(cultivar, year, number_from, number_to):
    return f"{config.INDENT}You have chosen to hold back {cultivar}\
    \n{config.INDENT}plants of age Year-{year}.\
    \n{config.INDENT}There are currently {number_from} plants of that category recorded\
    \n{config.INDENT}in the system.\
    \n{config.INDENT}There are now {number_to} plants of that cultivar listed as being a\
    \n{config.INDENT}year younger.\
    \n{config.INDENT}The specified number of plants will be held back for a year."

def successfully_held(number, cultivar, year, remaining, total):
    return f"{config.INDENT}Successfully recorded holding back {number} {cultivar}\
    \n{config.INDENT}plants of year-{year}.\
    \n{config.INDENT}You now have a remaining stock of {remaining} plants of that category\
    \n{config.INDENT}and a total stock of {total} of Year-{year - 1} plants of that cultivar."

def bring_chosen(cultivar, year, number_from, number_to):
    return f"{config.INDENT}You have chosen to bring forward {cultivar}\
    \n{config.INDENT}plants of age Year-{year}.\
    \n{config.INDENT}There are currently {number_from} plants of that category recorded\
    \n{config.INDENT}in the system.\
    \n{config.INDENT}There are now {number_to} plants of that cultivar listed as being\
     \n{config.INDENT}a year older.\
    \n{config.INDENT}The specified number of plants will be brought forward by a year."

def successfully_brought(number, cultivar, year, number_from, number_to):
    return f"{config.INDENT}Successfully recorded bringing forward {number} {cultivar}\
    \n{config.INDENT}plants of Year-{year}.\
    \n{config.INDENT}You now have a remaining stock of {number_from} plants of that category\
    \n{config.INDENT}and a total stock of {number_to} of year-{year + 1} plants of that cultivar."

def last_year(year):
    return f"{config.INDENT}The last year created was {year}."

def rootstocks_in_stock(cuttings, rootstocks):
    return f"\n{config.INDENT}Info: You took {cuttings} cuttings last year.\
        \n{config.INDENT}You now have {rootstocks} maturing rootstocks in stock."

def year_created(year, cuttings):
    return f"{config.INDENT}Year {year} created. {cuttings} cuttings planned\
        \n{config.INDENT}for this year."

def new_year_cancelled(new_year, old_year):
    return f"{config.INDENT}The year {new_year} has not been created.\
        \n{config.INDENT}The current year is still {old_year}"
