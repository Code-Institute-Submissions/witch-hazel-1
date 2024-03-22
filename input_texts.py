import config

Y_OR_N_TEXT = "Type 'y' for yes or 'n' for no:"

CHOOSE_CULTIVAR = f"{config.INDENT}Please enter the number of the cultivar for which you want to plan grafting\
    \n{config.INDENT}(see the cultivars listed above): \n"

ENTER_TO_CONTINUE = f"{config.INDENT}Press Enter to continue ..."

def new_planned_value(cultivar):
    return f"{config.INDENT}Type in the new planned value for {cultivar}: \n"

def record_how_many_cuttings(taken):
    f"{config.INDENT}How many cuttings have you now taken in addition to the ones\
        \n{config.INDENT}you've already recorded ({taken}): \n"

