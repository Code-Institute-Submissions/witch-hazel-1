import config

Y_OR_N_TEXT = "Type 'y' for yes or 'n' for no:"

CHOOSE_CULTIVAR_P = f"{config.INDENT}Please enter the number of the cultivar for which you want to plan grafting\
    \n{config.INDENT}(see the cultivars listed above): \n"

CHOOSE_CULTIVAR_M = f"{config.INDENT}Please enter the cultivar number of the new grafts you want to record\
    \n{config.INDENT}(see the cultivars listed above): \n"

ENTER_TO_CONTINUE = f"{config.INDENT}Press Enter to continue ..."

PLAN_CUTTINGS = f"{config.INDENT}Would you like to plan the number of cuttings you intend to take this season?\
                \n{Y_OR_N_TEXT}\n"

RECORD_POTTED = f"{config.INDENT}You have not yet potted up any cuttings! Would you like to record some newly potted cuttings now?\
            \n{Y_OR_N_TEXT}\n"

LOSS_OF_ROOTSTOCKS = f"{config.INDENT}Would you like to record a loss of new rootstocks?\
    \n{Y_OR_N_TEXT}\n"

CHOOSE_CULTIVAR_LOST = f"{config.INDENT}Please enter the cultivar number for which you want to record a loss\
        \n{config.INDENT}(see the cultivars listed above): \n"

CHOOSE_YEAR_LOST = f"{config.INDENT}Please enter the age of the plants for which you want to record a loss\
        \n{config.INDENT}(typing '1' for year-one plants, '2' for year-two plants, and so on): \n"

HOW_MANY_LOST = f"{config.INDENT}How many plants of that category have been lost since then? \n"

GAIN_OF_ROOTSTOCKS = f"{config.INDENT}Would you like to record an acquisition of new rootstocks?\
    \n{Y_OR_N_TEXT}\n"

HOW_MANY_ROOTSTOCKS_GAINED = f"{config.INDENT}How many rootstocks have been acquired since then? \n"

CHOOSE_CULTIVAR_GAINED = f"{config.INDENT}Please enter the cultivar number for which you want to enter an acquisition\
        \n{config.INDENT}(see the cultivars listed above): \n"

CHOOSE_YEAR_GAINED = "{config.INDENT}Please enter the age of the plants for which you want to enter an acquisition\
        \n{config.INDENT}(typing '1' for year-one plants, '2' for year-two plants, and so on): \n"

HOW_MANY_GAINED = f"{config.INDENT}How many plants of that category have been acquired since the last recorded entry? \n"

CHOOSE_CULTIVAR_HOLD = f"{config.INDENT}Please enter the cultivar number for which you want to hold plants back\
    \n{config.INDENT}(see the cultivars listed above): \n"

CHOOSE_YEAR_HOLD = f"{config.INDENT}Please enter the age of the plants that you want to hold back (typing '2'\
        \n{config.INDENT}for year-two plants or '3' for year-three plants, and so on): \n"

HOW_MANY_HELD = f"{config.INDENT}How many plants of that category do you want to hold back a year? \n"

CHOOSE_CULTIVAR_BRING = f"{config.INDENT}Please enter the cultivar number for which you want to bring plants forward\
    \n{config.INDENT}(see the cultivars listed above): \n"

CHOOSE_YEAR_BRING = f"{config.INDENT}Please enter the age of the plants for which you want to bring plants forward\
        \n{config.INDENT}(typing '1' for year-one plants or '2' for year-two plants, and so on): \n"

HOW_MANY_BROUGHT = f"{config.INDENT}How many plants of that category do you want to bring forward for a year? \n"


def new_planned_value(cultivar):
    return f"{config.INDENT}Type in the new planned value for {cultivar}: \n"

def record_how_many_cuttings(taken):
    return f"{config.INDENT}How many cuttings have you now taken in addition to the ones\
        \n{config.INDENT}you've already recorded ({taken}): \n"

def grafts_now_made(cultivar):
    return f"{config.INDENT}Type in the number of new grafts you have made of {cultivar}: \n"

def replace_value(planned_value, year):
    return f"{config.INDENT}So far you have planned to take {planned_value} cuttings for {year}! Would you like replace that number with a new one?\
                    \n{Y_OR_N_TEXT}\n"

def enter_planned_cuttings(last_year, last_year_rooted, planned_string, text_segment):
    return f"{config.INDENT}You took {last_year} cuttings last year, resulting in {last_year_rooted} successfully rooted cuttings.\
            {planned_string}\
            \n{config.INDENT}Enter a {text_segment}figure for planned cuttings for this year: \n"

def replace_value_confirm(cuttings_taken):
    return f"{config.INDENT}You have already taken {cuttings_taken} cuttings this year. This is more than your new planned figure!\
                \n{config.INDENT}Are you sure you want to replace the planned figure with this one?\
                \n{Y_OR_N_TEXT}\n"

def add_potted(cuttings_potted):
    return f"{config.INDENT}So far you have potted up {cuttings_potted} cuttings! Would you like to add to that number?\
            \n{Y_OR_N_TEXT}\n"

def how_many_potted(qualifier):
    return f"{config.INDENT}How many cuttings have you now potted up{qualifier}?\n"

    




