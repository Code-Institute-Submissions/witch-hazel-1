import config

Y_OR_N_TEXT = f"{config.INDENT}Type 'y' for yes or 'n' for no."

CHOOSE_CULTIVAR_P = f"{config.INDENT}Please enter the number of the cultivar for which you want to plan\
    \n{config.INDENT}grafting (see the cultivars listed above). \
    \n\n{config.PROMPT_STRING}"

CHOOSE_CULTIVAR_M = f"{config.INDENT}Please enter the cultivar number of the new grafts you want to record\
    \n{config.INDENT}(see the cultivars listed above). \
    \n\n{config.PROMPT_STRING}"

PLAN_CUTTINGS = f"{config.INDENT}Would you like to plan the number of cuttings you intend to take this season?\
    \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

RECORD_POTTED = f"{config.INDENT}You have not yet potted up any cuttings! Would you like to record some\
    \n{config.INDENT}newly potted cuttings now?\
    \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

LOSS_OF_ROOTSTOCKS = f"{config.INDENT}Would you like to record a loss of new rootstocks?\
    \n{config.INDENT}If you want to record a loss of grafted plants, choose 'n'!\
    \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

CHOOSE_CULTIVAR_LOST = f"{config.INDENT}Please enter the cultivar number for which you want to record a loss\
    \n{config.INDENT}(see the cultivars listed above). \
    \n\n{config.PROMPT_STRING}"

CHOOSE_YEAR_LOST = f"{config.INDENT}Please enter the age of the plants for which you want to record a loss\
    \n{config.INDENT}(typing '1' for year-one plants, '2' for year-two plants, and so on). \
    \n\n{config.PROMPT_STRING}"

HOW_MANY_PLANTS_LOST = f"{config.INDENT}How many plants of that category have been lost since then? \
    \n\n{config.PROMPT_STRING}"

GAIN_OF_ROOTSTOCKS = f"{config.INDENT}Would you like to record an acquisition of new rootstocks?\
    \n{config.INDENT}If you want to record an acquisition of new grafted plants, choose 'n'!\
    \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

HOW_MANY_ROOTSTOCKS_GAINED = f"{config.INDENT}How many rootstocks have been acquired since then? \
    \n\n{config.PROMPT_STRING}"

CHOOSE_CULTIVAR_GAINED = f"{config.INDENT}Please enter the cultivar number for which you want to\
    \n{config.INDENT}enter an acquisition (see the cultivars listed above).\
    \n\n{config.PROMPT_STRING}"

CHOOSE_YEAR_GAINED = f"{config.INDENT}Please enter the age of the plants for which you want to\
    \n{config.INDENT}enter an acquisition (typing '1' for year-one plants, '2' for year-two plants,\
    \n{config.INDENT}and so on).\
    \n\n{config.PROMPT_STRING}"

HOW_MANY_GAINED = f"{config.INDENT}How many plants of that category have been acquired since the \
    \n{config.INDENT}last recorded entry? \
    \n\n{config.PROMPT_STRING}"

CHOOSE_CULTIVAR_HOLD = f"{config.INDENT}Please enter the cultivar number for which you want to\
    \n{config.INDENT}hold plants back (see the cultivars listed above).\
    \n\n{config.PROMPT_STRING}"

CHOOSE_YEAR_HOLD = f"{config.INDENT}Please enter the age of the plants that you want to hold back\
    \n{config.INDENT}(typing '2' for year-two plants or '3' for year-three plants, and so on). \
    \n\n{config.PROMPT_STRING}"

HOW_MANY_HELD = f"{config.INDENT}How many plants of that category do you want to hold back a year? \
    \n\n{config.PROMPT_STRING}"

CHOOSE_CULTIVAR_BRING = f"{config.INDENT}Please enter the cultivar number for which you want to\
    \n{config.INDENT}bring plants forward (see the cultivars listed above). \
    \n\n{config.PROMPT_STRING}"

CHOOSE_YEAR_BRING = f"{config.INDENT}Please enter the age of the plants for which you want to\
    \n{config.INDENT}bring plants forward(typing '1' for year-one plants or '2' for year-two\
    \n{config.INDENT}plants, and so on).\
    \n\n{config.PROMPT_STRING}"

HOW_MANY_BROUGHT = f"{config.INDENT}How many plants of that category do you want to bring\
    \n{config.INDENT}forward for a year?\
    \n\n{config.PROMPT_STRING}"

NO_GRAFTS_YET_MADE = f"{config.INDENT}You have not yet made any grafts of this cultivar.\
    \n{config.INDENT}Would you like record some grafts now?\
    \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

NO_GRAFTS_YET_PLANNED = f"{config.INDENT}You have not yet planned to make any grafts\
    \n{config.INDENT}of this cultivar. Would you like to do so now?\
    \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

TAKE_MORE_CUTTINGS = f"{config.INDENT}Would you like to add additional cuttings taken now?\
        \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

HOW_MANY_ROOTSTOCKS_LOST = f"{config.INDENT}How many rootstocks have been lost since then? \
    \n\n{config.PROMPT_STRING}"

def grafts_made(grafts):
    return f"{config.INDENT}You have already made {grafts} grafts of this cultivar.\
            \n{config.INDENT}Would you like to add to this value?\
            \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

def completed_for_year(task):
    return f"{config.INDENT}Have you completed the '{task}'\
        \n{config.INDENT}task for the year?\
        \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

def new_planned_value(cultivar):
    return f"{config.INDENT}Type in the new planned value for {cultivar}. \
        \n\n{config.PROMPT_STRING}"

def record_how_many_cuttings(qualifier_clause):
    return f"{config.INDENT}How many cuttings have you now taken{qualifier_clause}? \
        \n\n{config.PROMPT_STRING}"

def cuttings_in_addition(taken):
    return f" in addition to the ones\
        \n{config.INDENT}you've already recorded ({taken})"

def replace_graft_value(old_value):
    return f"{config.INDENT}So far, you have planned to make {old_value} grafts\
        \n{config.INDENT}of this cultivar. Would you like to replace this value? \
        \n\n{config.PROMPT_STRING}"

def task_closed_reopen(task):
    return f"\n{config.INDENT}The task '{task}' has been\
        \n{config.INDENT}closed for the year. Would you like to reopen it?\
        \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

def grafts_now_made(cultivar):
    return f"{config.INDENT}Type in the number of new grafts you have made of\
    \n{config.INDENT}{cultivar}. \
        \n\n{config.PROMPT_STRING}"

def replace_value(planned_value, year):
    return f"{config.INDENT}So far you have planned to take {planned_value} cuttings for {year}!\
        \n{config.INDENT}Would you like replace that number with a new one?\
        \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

def enter_planned_cuttings(last_year, last_year_rooted, planned_string, text_segment):
    return f"{config.INDENT}You took {last_year} cuttings last year, resulting in\
        \n{config.INDENT}{last_year_rooted} successfully rooted cuttings.\
        {planned_string}\
        \n{config.INDENT}Enter a {text_segment}figure for planned cuttings for this year. \
        \n\n{config.PROMPT_STRING}"

def replace_value_confirm(cuttings_taken):
    return f"{config.INDENT}You have already taken {cuttings_taken} cuttings this year.\
        \n{config.INDENT}This is more than your new planned figure!\
        \n{config.INDENT}Are you sure you want to replace the planned figure with this one?\
        \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

def add_potted(cuttings_potted):
    return f"{config.INDENT}So far you have potted up {cuttings_potted} cuttings!\
    \n{config.INDENT}Would you like to add to that number?\
        \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

def how_many_potted(qualifier):
    return f"{config.INDENT}How many cuttings have you now potted up{qualifier}? \
        \n\n{config.PROMPT_STRING}"

def create_new_year(new_year):
    return f"{config.INDENT}Would you like to create a record for {new_year}?\
        \n{Y_OR_N_TEXT}\n{config.PROMPT_STRING}"

def how_many_cuttings(new_year):
    return f"{config.INDENT}How many cuttings would you like to plan for {new_year}? \
        \n{config.INDENT}(Enter 0 if you want to plan cutting numbers later). \
        \n\n{config.PROMPT_STRING}"

    




