import gspread
import help_texts
import input_texts
import msgs
import config
import error_msgs
import commands
from google.oauth2.service_account import Credentials
import sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hamamelis')

rootstock = SHEET.worksheet('rootstock')
grafts_year_zero = SHEET.worksheet('grafts-year-zero')
plants = SHEET.worksheet('plants')
completed = SHEET.worksheet('completed')

row_values = plants.row_values(1)
# Find the column to stop at (first column on the plants page that contains no data).
first_empty_index = next((i for i,
                        val in enumerate(row_values) if not val),
                        len(row_values))
last_column = chr(ord('a') + first_empty_index)

name_range = f"a1:{last_column}1"  # Names of cultivars
cultivars = plants.get(name_range)[0]

cuttings_taken = int(rootstock.acell('c2').value)
rootstocks_potted = int(rootstock.acell('d2').value)
mature_rootstocks = int(rootstock.acell('e2').value)


rootstock_data = rootstock.get_all_values()
grafts_data = grafts_year_zero.get_all_values()
plants_data = plants.get_all_values()
completed_data = completed.get_all_values()


def list_cultivars(cultivar_list):
    count = 0
    for cultivar in cultivar_list:
        count += 1
        print(f"{count}. {cultivar}")


def exit_program():
    print(f"{config.INDENT}{msgs.EXIT_MSG}")
    sys.exit(0)


"""
This function closes out each individual task for the year.
When all tasks are closed out, you can create a new year (Option 0)
"""

def completed_for_year(affected_cell, affected_task):
    if input(f"{config.INDENT}{msgs.AFFECTED_TASK_COMPLETED}\
    \n{config.INDENT}{input_texts.Y_OR_N_TEXT}: \n").lower() ==commands.YES:
        completed.update_acell(affected_cell, 'y')
        print(msgs.task_completed(affected_task))
    else:
        print(msgs.task_not_completed(affected_task))
    
def parse_cell_data():
    exit(0)


"""
This recursive function does one of the following things:
- It returns a number if the user input is convertible into a non-negative integer.
- It returns nothing and exits the program if the user input parses to "exit".
- It returns nothing and goes to the general_help function if the user input parses to "help".
- It returns nothing and goes to the appropriate detailed help function if the user input parses to "help [n]" (where [n] is an integer
  between 0 and the number of options available in the program)
- If the user input is anything else, it calls itself, asking the user to enter number within the allowable range or some other valid
  input.
The arguments it takes are fairly self-explanatory.
"""

def parse_user_input(user_input, mini=0, maxi=10000, not_a_number_blurb=error_msgs.DEFAULT_NOT_A_NUMBER_BLURB, 
        not_in_range_blurb=error_msgs.DEFAULT_NOT_IN_RANGE_BLURB):
    try:
        number = int(user_input)
        if mini <= number <= maxi:
            return number
        else:
            return parse_user_input(input(msgs.a_and_b(f"{config.INDENT}{not_in_range_blurb}{mini}",{maxi})),mini, maxi)
    except:
        if user_input=='':
            return parse_user_input(input(msgs.a_and_b(f"{config.INDENT}'{user_input}'{not_a_number_blurb}{mini}",{maxi})), mini, maxi)
        elif user_input.lower()==commands.EXIT:
            exit_program()
        elif user_input.lower()==commands.HELP:
            general_help()
        elif user_input.lower().split()[0]==commands.HELP:
            if mini <= int(user_input.lower().split()[1]) <= maxi:
                print(f"{config.INDENT}{msgs.detailed_help_choice(user_input.split()[1])}")
                option_help(int(user_input.split()[1]))
        else:
            return parse_user_input(input(msgs.a_and_b(f"{config.INDENT}{not_a_number_blurb}{mini}",{maxi})), mini, maxi)

def Get_survival_rate(start_num, end_num):
    if int(start_num) == 0:
        return f'{config.INDENT}{error_msgs.NO_START_NUMBER}'
    elif int(end_num) > int(start_num):
        return f'{config.INDENT}{error_msgs.MORE_THAN_INITIAL}'
    else:
        return int(end_num) / int(start_num)

cutting_success = Get_survival_rate(cuttings_taken, rootstocks_potted)
potting_success = Get_survival_rate(rootstocks_potted, mature_rootstocks)

lower_bound = 0
upper_bound = 9

def startup_instructions():
    """
    Welcomes the user to the app.
    Presents general info on it.
    """

    print(help_texts.intro_text)
    input(f"{config.INDENT}{msgs.ANY_KEY_MSG}")
    print(config.CURSOR_UP_ONE + config.ERASE_LINE)
    main_menu()

def main_menu():
    """
    The program's main menu on startup and after every option or help message.
    """

    print(help_texts.menu_title)
    print(help_texts.menu_text)

    while True:
        user_input = parse_user_input(input(msgs.main_menu_prompt(lower_bound, upper_bound)), lower_bound, upper_bound)
        if user_input:
            execute_option(user_input)


def general_help():
    """
    General help messages on how to use the app print to screen one after another
    """
    print(help_texts.help_text1)
    input(f"{config.INDENT}{msgs.MORE_GEN_HELP}")
    print(help_texts.help_text2)
    main_menu()


def option_help(option_no):
    """
    Specific help messages for each option
    """
    if option_no==0:
        print(help_texts.help_text_option0)

    elif option_no == 1:
        print(help_texts.help_text_option1)

    elif option_no == 2:
        print(help_texts.help_text_option2)

    elif option_no == 3:
        print(help_texts.help_text_option3)

    elif option_no == 4:
        print(help_texts.help_text_option4)

    elif option_no == 5:
        print(help_texts.help_text_option5)

    elif option_no == 6:
        print(help_texts.help_text_option6)

    elif option_no == 7:
        print(help_texts.help_text_option7)

    elif option_no == 8:
        print(help_texts.help_text_option8)

    elif option_no == 9:
        print(help_texts.help_text_option9)

    else:
        print(msgs.SPECIFIC_HELP_PROMPT)
    input
    

def execute_option(input):
    """
    Executes the option typed in by the user
    on condition it's valid.
    """

    print(config.LINE_OF_UNDERSCORES)
    if input == 1:
        print(f"{config.INDENT}{msgs.PLAN_GRAFTS}")
        plan_grafting_campaign()
    elif input == 2:
        print(f"{config.INDENT}{msgs.TAKE_GRAFTS}")
        record_grafts()
    elif input == 3:
        print(f"{config.INDENT}{msgs.POT_UP_CUTTINGS}")
        record_potted_cuttings()
    elif input == 4:
        print(f"{config.INDENT}){msgs.PLAN_CUTTINGS}")
        plan_cutting_campaign()
    elif input == 5:
        print(f"{config.INDENT}{msgs.TAKE_CUTTINGS}")
        record_cuttings_taken()
    elif input == 6:
        print(f"{config.INDENT}{msgs.RECORD_LOSS}")
        record_loss()
    elif input == 7:
        print(f"{config.INDENT}{msgs.RECORD_ACQ}")
        record_gain()
    elif input == 8:
        print(f"{config.INDENT}{msgs.HOLD_BACK}")
        hold_back()
    elif input == 9:
        print(f"{config.INDENT}{msgs.BRING_FORWARD}")
        bring_forward()
    elif input == 0:
        print(f"{config.INDENT}{msgs.NEW_YEAR}")
        create_year()
    else:
        print(error_msgs.valid_option_number(lower_bound, upper_bound))
    main_menu()


def complete_cuttings_taken_record(taken, planned):
    
    if taken >= planned:
        print(planned_cuttings_taken(taken, planned))
    else:
        if taken > 0:
            info_msg = msgs.cuttings_taken(taken, planned)
            prompt_msg = input_texts.TAKE_MORE_CUTTINGS
        else:
            info_msg = msgs.no_cuttings_yet_taken(planned)
            prompt_string = msgs.TAKE_CUTTINGS_NOW

    if input(input_string).lower() == commands.YES:
        taken += parse_user_input(input(record_how_many_cuttings(input_texts.record_how_many_cuttings(taken))))
        rootstock.update_acell('c2', taken)
        if taken >= planned:
            print(msgs.planned_cuttings_reached(planned, taken))
        else:
            print(msgs.planned_cuttings_not_reached(planned, taken))

        print(msgs.CUTTINGS_SUCCESSFUL)
        print(msgs.a_out_of_b(taken, planned))
        run_cuttings_session(taken)
    else:
        print(msgs.CANCEL_TAKE_CUTTINGS)
    
    print(BACK_TO_MENU)
    input()
    main_menu()

def check_is_complete(cell, task):
    complete = completed.acell(cell).value.lower()
    if complete == 'y':
        if input(msgs.task_closed_reopen(task)).lower() == commands.YES:
            print(msgs.REOPENING)
            completed.update_acell(cell, 'n')
            return False
        else:
            print(msgs.do_not_reopen(task))
            return True
    else:
        return False

def plan_grafting_campaign():
    """
    Option 1:
    Lets user add a planned number of grafts for each cultivar.
    Should be used in late winter (February or March).
    Shows the number of rootstocks ready for grafting and the number left.
    Warns the user when they're planning to use more rootstocks than they have.
    """
    rootstocks_available = int(rootstock.acell('g4').value)
    rootstocks_in_stock = int(rootstock.acell('f4').value)

    row_values = grafts_year_zero.row_values(1)
    # Find the column to stop at (first column that contains no data)
    first_empty_index = next((i for i,
                              val in enumerate(row_values) if not val),
                             len(row_values))
    last_column = chr(ord('a') + first_empty_index)

    name_range = f"c1:{last_column}1"
    planned_range = f"c2:{last_column}2"
    grafted_range = f"c3:{last_column}3"
    stock_range = f"c4:{last_column}4"

    cultivars = grafts_year_zero.get(name_range)[0]
    planned_numbers = grafts_year_zero.get(planned_range)[0]
    """
    Converts planned number strings into integers
    and adds them together.
    """
    planned_numbers = [int(x) for x in planned_numbers]
    total_planned = sum(planned_numbers)

    print(msgs.WHICH_CULTIVAR_P)

    # List out the cultivars you have in your data in an ordered list.
    list_cultivars(cultivars)

    cultivar_value = parse_user_input(input(input_texts.CHOOSE_CULTIVAR), 1, count)
    current_cultivar = cultivars[cultivar_value-1]
    address_current_cultivar  = f"{chr(ord('c') + cultivar_value - 1)}2"
    task_check_complete_address = f"{chr(ord('d') + cultivar_value - 1)}2"
    task_string = plan_for(current_cultivar)

    if check_is_complete(task_check_complete_address, f"{task_string}") == False:
        print(msgs.planned_for(current_cultivar))
        print(msgs.rootstocks_unplanned(rootstocks_in_stock,rootstocks_available + planned_numbers[cultivar_value - 1])) 

        if planned_numbers[cultivar_value - 1] > 0:
            info_msg = replace_value(planned_numbers[cultivar_value - 1]) 
        else:
            info_msg = msgs.NO_GRAFTS_YET_TAKEN
        if input(info_msg).lower() == commands.YES:
            new_planned_value = parse_user_input(input(input_texts.new_planned_value(current_cultivar)))
            grafts_year_zero.update_acell(address_current_cultivar, new_planned_value)
            print(msgs.planned_grafts_changed(current_cultivar, new_planned_value))
            completed_for_year(f"{chr(ord('d') + cultivar_value - 1)}2", f"{task_string}")

        else:
            print(msgs.task_cancelled(task_string, current_cultivar))
            completed_for_year(task_check_complete_address, task_string)
    
    print(input_texts.ENTER_TO_CONTINUE)
    input()


def record_grafts():
    """
    Option 2:
    Lets user record the number of grafts taken for a chosen cultivar.
    Should be used in late winter; at grafting time.
    Shows the total for rootstocks ready for grafting and the number left.
    Warns the user when they've used more rootstocks than they actually have.
    """
    rootstocks_in_stock = int(rootstock.acell('f4').value)
    rootstocks_available = int(rootstock.acell('g4').value)


    row_values = grafts_year_zero.row_values(1)

    # Find the column to stop at (first column that contains no data).
    first_empty_index = next((i for i,
                              val in enumerate(row_values) if not val),
                             len(row_values))
    last_column = chr(ord('a') + first_empty_index)

    name_range = f"c1:{last_column}1"  # Names of cultivars
    planned_range = f"c2:{last_column}2"  # Numbers of planned grafts
    grafted_range = f"c3:{last_column}3"  # Plants already grafted

    cultivars = grafts_year_zero.get(name_range)[0]
    planned_numbers = grafts_year_zero.get(planned_range)[0]
    # Converts the strings in the planned numbers list into integers
    # to make it possible to sum them together.
    planned_numbers = [int(x) for x in planned_numbers]
    grafts_this_year = grafts_year_zero.get(grafted_range)[0]
    grafts_this_year = [int(x) for x in grafts_this_year]
    total_grafted = sum(grafts_this_year)

    print(WHICH_CULTIVAR_M)
    # List out the names of the cultivars you have in your data
    # in an ordered list.
    
    list_cultivars(cultivars)

    print(f"\n{config.INDENT}For which cultivar have you made grafts?\n")

    cultivar_value = parse_user_input(input(f"{config.INDENT}Please enter the cultivar number of the new grafts you want to record\
    \n{config.INDENT}(see the cultivars listed above): \n"), 1, count)
    task_check_complete_address = f"{chr(ord('d') + cultivar_value - 1)}3"
    current_cultivar = cultivars[cultivar_value - 1]
    address_current_cultivar = f"{chr(ord('c') + cultivar_value - 1)}3"
    task_string = f"make grafts for {current_cultivar}"
    address_rootstocks = 'f3'

    if check_is_complete(task_check_complete_address, f"{task_string}") == False:
        grafts_this_cultivar = grafts_this_year[cultivar_value - 1]
        planned_this_cultivar = planned_numbers[cultivar_value -1]
        print(f"{config.INDENT}You have chosen to record grafts of {current_cultivar}\
        \n")
        print (f"{config.INDENT}You have planned to make {planned_this_cultivar} of this cultivar.")
        if grafts_this_cultivar > 0:
            confirm_string = f" You have already made {grafts_this_cultivar} grafts of this cultivar.\
            \n{config.INDENT}Would you like to add to this value?\
            \n{input_texts.Y_OR_N_TEXT}\n"
        else:
            confirm_string = f"{config.INDENT}You have not yet made any grafts of this cultivar.\
            \n{config.INDENT}Would you like record some grafts now?\
            \n{input_texts.Y_OR_N_TEXT}\n"
        if input(confirm_string).lower() == commands.YES:
            newly_made_grafts = parse_user_input(input(f"{config.INDENT}Type in the number of new grafts you have made of {current_cultivar}: \n"))
            grafts_this_cultivar += newly_made_grafts
            grafts_year_zero.update_acell(address_current_cultivar, int(grafts_this_cultivar))
            print()
            print(f"{config.INDENT}Number of grafts made for {current_cultivar} successfully changed.\
                \n{config.INDENT}The new total of grafts made this year for this cultivar is {grafts_this_cultivar}.\
                \n{config.INDENT}You originally planned to make {planned_this_cultivar}.\
                \n{config.INDENT}Successfully completed record of new grafts made.")
            completed_for_year(task_check_complete_address, f"{task_string}")
        else:
            print(f"{config.INDENT}Plan grafts action for {current_cultivar} cancelled.\
            \n{config.INDENT}No changes have been made to the data.")
            completed_for_year(task_check_complete_address, task_string)
    
    print(f"{config.INDENT}Press Enter to continue ...")
    input()


def record_potted_cuttings():
    """
    Option 3:
    Lets user record progress in potting up the successfully rooted cuttings
    (taken the previous Autumn).
    Ideally used daily during the potting campaign (in the Spring).
    """
    cuttings_taken = int(rootstock.acell('c3').value)
    cuttings_potted = int(rootstock.acell('d3').value)
    new_rootstocks = int(rootstock.acell('f3').value)

    if check_is_complete('c3', "potting rooted cuttings") == False:
        if cuttings_potted > 0:
            confirm_string = f"{config.INDENT}So far you have potted up {cuttings_potted} cuttings! Would you like to add to that number?\
            \n{input_texts.Y_OR_N_TEXT}\n"
            qualifier_clause = f" in addition to the ones\
            \n{config.INDENT}you have already recorded"
        else:
            confirm_string = f"{config.INDENT}You have not yet potted up any cuttings! Would you like to record some newly potted cuttings now?\
            \n{config.INDENT}{input_texts.Y_OR_N_TEXT}\n"
            qualifier_clause = ""
        if input(confirm_string).lower() == commands.YES:
            newly_potted = parse_user_input(input(f"{config.INDENT}How many cuttings have you now potted up{qualifier_clause}?\n"))
            if cuttings_potted + newly_potted > cuttings_taken:
                print(f"{config.INDENT}If {newly_potted} is added to the existing figure of newly rooted cuttings ({new_rootstocks}), then you'll\
                \n{config.INDENT}have potted up more cuttings than you took in the Autumn ({cuttings_taken}).\
                \n{config.INDENT}That is not possible. The absolute maximum number you can pot up in this session is {cuttings_taken - cuttings_potted}.\
                \n{config.INDENT}Action cancelled. No changes have been made to the data.")
            else:
                cuttings_potted += newly_potted
                rootstock.update_acell('d3', cuttings_potted)
                print(f"{config.INDENT}You have now potted up a total of {cuttings_potted} cuttings out of a total of {cuttings_taken} (minus\
                \n{config.INDENT}any that have failed to root)!\
                \n{config.INDENT}You will use them as rootstocks during the grafting campaign next season (once\
                \n{config.INDENT}they have established themselves in their pots).")
                completed_for_year('c3', 'pot up rooted cuttings')
        else:
            print(f"{config.INDENT}Record new cuttings potted action cancelled.\
            \n{config.INDENT}No changes have been made to the data.")
            completed_for_year('c3', 'pot up rooted cuttings')

    print(f"{config.INDENT}Press Enter to continue ...")
    input()

def run_cuttings_plan(cuttings):
    rootstock.update_acell('b2', cuttings)
    print(f"{config.INDENT}Number of cuttings planned for this year successfully changed.")
    completed_for_year('b2', 'plan cutting numbers')

def  cancel_cuttings_plan():
    print(f"{config.INDENT}Plan cuttings action cancelled.\
        \nNo changes have been made to the data.")

def run_cuttings_session(cuttings):
    rootstock.update_acell('c2', cuttings)
    print(f"{config.INDENT}Successfully added to number of cuttings taken so far in this campaign.")
    completed_for_year('b3', 'record cuttings taken')



def plan_cutting_campaign():
    """
    Option 4:
    Helps plan cuttings task
    """
    planned_cuttings = int(rootstock.acell('b2').value)
    last_year_cuttings = int(rootstock.acell('c3').value)
    last_year_rooted_cuttings = int(rootstock.acell('d3').value)
    this_year_cuttings_taken = int(rootstock.acell('c2').value)
    current_year = int(rootstock.acell('a2').value)
    task = 'planning cuttings'
    if check_is_complete('b2', task) == False:
        if int(planned_cuttings) > 0:
            user_confirmation = input(f"{config.INDENT}So far you have planned to take {planned_cuttings} cuttings for {current_year}! Would you like replace that number with a new one?\
                    \n{input_texts.Y_OR_N_TEXT}\n").lower()
            planned_cuttings_string = f"\n{config.INDENT}The present planned figure for this year is {planned_cuttings}."
            text_segment = "new "
        else:
            user_confirmation = input(f"{config.INDENT}Would you like to plan the number of cuttings you intend to take this season?\
                \n{input_texts.Y_OR_N_TEXT}\n").lower()
            planned_cuttings_string = ""
            text_segment = ""
        if user_confirmation == commands.YES:
            planned_cuttings = parse_user_input(input(f"{config.INDENT}You took {last_year_cuttings} cuttings last year, resulting in {last_year_rooted_cuttings} successfully rooted cuttings.\
            {planned_cuttings_string}\
            \n{config.INDENT}Enter a {text_segment}figure for planned cuttings for this year: \n"))
            if planned_cuttings <= this_year_cuttings_taken:
                user_confirmation = input(f"{config.INDENT}You have already taken {this_year_cuttings_taken} cuttings this year. This is more than your new planned figure!\
                \n{config.INDENT}Are you sure you want to replace the planned figure with this one?\
                \n{input_texts.Y_OR_N_TEXT}\n").lower()
                if user_confirmation == commands.YES:
                    run_cuttings_plan(planned_cuttings)
                else:
                    cancel_cuttings_plan()
            else:
                run_cuttings_plan(planned_cuttings)
        else:
            cancel_cuttings_plan()
            completed_for_year('B2', task)

    print(f"{config.INDENT}Press Enter to continue ...")
    input()


def record_cuttings_taken():
    """
    Option 5:
    Lets the user record cuttings actually taken.
    Ideally used daily during the cuttings campaign (in Autumn).
    """
    if check_is_complete('b3', 'taking cuttings') == False:
        cuttings_taken = int(rootstock.acell('c2').value)
        cuttings_planned = int(rootstock.acell('b2').value)
        cuttings_rooted = int(rootstock.acell('d2').value)
        complete_cuttings_taken_record(cuttings_taken, cuttings_planned)

    completed_for_year('B2', task)

    print(f"{config.INDENT}Press Enter to continue ...")
    input()


def record_loss():
    """
    Option 6:
    Lets user record losses in stocks for any cultivar in any year.
    Works for both rooted cuttings and grafted cultivars.
    May be used throughout the year.
    Losses of cuttings are not recorded until the time comes to pot
    up those of them that have rooted successfully.
    """
    # Did we lose new_rootstocks?
    if input(f"{config.INDENT}Would you like to record a loss of new rootstocks?\
    \n{input_texts.Y_OR_N_TEXT}\n").lower() == commands.YES:
        address_affected = 'e1'
        total_rootstocks = int(rootstock.acell(address_affected).value)

        print(f"{config.INDENT}At the last count there were {total_rootstocks} new rootstocks in the nursery")

        while True:
            number_lost = input("How many rootstocks have been lost since then? \n")
            try:
                number_lost = int(number_lost)
                if 0 <= number_lost <= total_rootstocks:
                    break
                else:
                    print(f"{config.INDENT}You can't have lost more rootstocks than you actually had in the nursery!\
                    \n{config.INDENT}Please enter an integer between 0 and\
                    {total_rootstocks}: ")
            except ValueError:
                print(f"{config.INDENT}Your number must be a positive integer or 0. Negative and decimal-point numbers,\
                \n{config.INDENT}text and special characters, etc. are not allowed: ")

        rootstock.update_acell(address_affected,
                               total_rootstocks - number_lost)
        print(f"{config.INDENT}Loss of {number_lost} new rootstocks recorded.\
        \n{config.INDENT}You now have a stock of {rootstock.acell(address_affected).value} new rootstocks.")
    else:
        """
        If what's been lost is grafted plants
        First define the cultivar affected
        """
        row_values = plants.row_values(1)
        # Find the column to stop at (first column that contains no data).
        first_empty_index = next((i for i,
                                  val in enumerate(row_values) if not val),
                                 len(row_values))
        last_column = chr(ord('a') + first_empty_index)

        name_range = f"a1:{last_column}1"  # Names of cultivars
        cultivars = plants.get(name_range)[0]

        # List the names of the cultivars in the data in an ordered list.
        print(f"{config.INDENT}For which cultivar would you like record a loss?")
        list_cultivars(cultivars)

        cultivar_value = parse_user_input(input(f"{config.INDENT}Please enter the cultivar number for which you want to record a loss\
        \n{config.INDENT}(see the cultivars listed above): \n"))
        affected_year = parse_user_input(input(f"{config.INDENT}Please enter the age of the plants for which you want to record a loss\
        \n{config.INDENT}(typing '1' for year-one plants, '2' for year-two plants, and so on): \n"))
        current_cultivar = cultivars[cultivar_value - 1]
        address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 1}"

        current_number = int(plants.acell(address_affected).value)
        print(f"{config.INDENT}You have chosen to register a loss of {current_cultivar} of age year-{affected_year}.\
        \n{config.INDENT}There are currently {current_number} plants of that category\
        \n{config.INDENT}recorded in the system.")
        while True:
            number_lost = input(f"{config.INDENT}How many plants of that category have been lost since then? \n")
            try:
                number_lost = int(number_lost)
                if 0 <= number_lost <= current_number:
                    break
                else:
                    print(f"{config.INDENT}You can't have lost more plants of this category than you actually had in the nursery!\
                    \n{config.INDENT}Please enter an integer between 0 and {current_number}.")
            except ValueError:
                print(f"{config.INDENT}Your number must be a positive integer or 0.\
                \n{config.INDENT}Negative and decimal-point numbers, text and special characters, etc. \
                \n{config.INDENT}are not allowed: ")
        current_number -= number_lost
        plants.update_acell(address_affected, current_number)
        print(f"{config.INDENT}Loss of {number_lost} {current_cultivar} of year-{affected_year} recorded.\
        \n{config.INDENT}You now have a remaining stock of {plants.acell(address_affected).value} plants of that category.")

        # number_lost
    print(f"{config.INDENT}Loss recorded successfully.")

    print(f"{config.INDENT}Press Enter to continue ...")
    input()


def record_gain():
    """
    Option 7:
    Essentially the opposite of Option 7.
    """
    # Did we acquire new_rootstocks ...?
    if input(f"{config.INDENT}Would you like to record an acquisition of new rootstocks?\
    \n{input_texts.Y_OR_N_TEXT}\n").lower() == commands.YES:
        address_affected = 'e1'
        total_rootstocks = int(rootstock.acell(address_affected).value)

        print(f"At the last count there were {total_rootstocks} \
        \n{config.INDENT}new rootstocks in the nursery")

        while True:
            number_gained = input(f"{config.INDENT}How many rootstocks have\
            \n{config.INDENT}been acquired since then? \n")
            try:
                number_gained = int(number_gained)
                break
            except ValueError:
                print(f"{config.INDENT}Your number must be a positive integer or 0.\
                \n{config.INDENT}Negative and decimal-point numbers, text and special characters, \
                \n{config.INDENT}etc. are not allowed: ")

        rootstock.update_acell(address_affected,total_rootstocks + number_gained)
        print(f"{config.INDENT}Acquisition of {number_gained} new rootstocks recorded.\
        \n{config.INDENT}You now have a stock of {rootstock.acell(address_affected).value}\
        \n{config.INDENT}new rootstocks.")
    else:
        """
        If what's been gained is grafted plants
        First define the cultivar affected
        """
        row_values = plants.row_values(1)
        # Find the column to stop at (first column that contains no data).
        first_empty_index = next((i for i,
                                  val in enumerate(row_values) if not val),
                                 len(row_values))
        last_column = chr(ord('a') + first_empty_index)

        name_range = f"a1:{last_column}1"  # Names of cultivars
        cultivars = plants.get(name_range)[0]

        # List the cultivars in the data in an ordered list.
        print(f"{config.INDENT}For which cultivar would you like record an acquisition?")
        list_cultivars(cultivars)

        cultivar_value = parse_user_input(input(f"{config.INDENT}Please enter the cultivar number for which you want to enter an acquisition\
        \n{config.INDENT}(see the cultivars listed above): \n"), 1, count)
        affected_year = parse_user_input(input(f"{config.INDENT}Please enter the age of the plants for which you want to enter an acquisition\
        \n{config.INDENT}(typing '1' for year-one plants, '2' for year-two plants, and so on): \n"), 1, 5)
        address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 1}"
        current_cultivar = cultivars[cultivar_value - 1]
        current_number = int(plants.acell(address_affected).value)
        print(f"{config.INDENT}You have chosen to register an acquisition of {current_cultivar} of age year-{affected_year}.\
        \n{config.INDENT}There are currently {current_number} plants of that category recorded in the system.")
        while True:
            number_gained = input(f"{config.INDENT}How many plants of that category have been acquired since the last recorded entry? \n")
            try:
                number_gained = int(number_gained)
                break
            except ValueError:
                print(error_msgs.POSITIVE_INT)
        current_number += number_gained
        plants.update_acell(address_affected, current_number)
        print(f"{config.INDENT}Acquisition of {number_gained} {current_cultivar} of year-{affected_year} recorded.\
        \n{config.INDENT}You currently have a stock of {plants.acell(address_affected).value} plants of that category.")

        # number_lost
    print(f"{config.INDENT}Acquisition recorded successfully.")
    
    print(f"{config.INDENT}Press Enter to continue ...")
    input('')


def hold_back():
    """
    Option 8:
    Essentially a Option 7 with a twist.
    Results in the given number of the chosen cultivar from year n
    being removed and then added to year n-1.
    """

    # List out the cultivars in the data in an ordered list.
    print(f"{config.INDENT}For which cultivar would you like hold back plants?")
    list_cultivars(cultivars)

    cultivar_value = parse_user_input(input(f"{config.INDENT}Please enter the cultivar number for which you want to hold plants back (see\
    \n{config.INDENT}the cultivars listed above): \n"))
    while True:
        affected_year = parse_user_input(input(f"{config.INDENT}Please enter the age of the plants that you want to hold back (typing '2'\
        \n{config.INDENT}for year-two plants or '3' for year-three plants, and so on): \n"))
        try:
            affected_year = int(affected_year)
            if affected_year > 1:
                break
            elif affected_year == 1:
                print(f"{config.INDENT}Year-one plants cannot be held back. Enter 2 or higher. But remember there's\
                \n{config.INDENT}no point in entering an age greater than the age of the nursery.")
            else:
                print(f"{config.INDENT}Please enter an integer between 2 and the age of the nursery.")
        except ValueError:
            print(f"{config.INDENT}Your number must be an integer greater than 2 and less than the age of the\
            \n{config.INDENT}nursery. Negative and decimal-point numbers, text and special characters, etc.\
            \n{config.INDENT}are not allowed: ")

    current_cultivar = cultivars[cultivar_value - 1]
    from_address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 1}"
    to_address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year}"

    current_number_from = int(plants.acell(from_address_affected).value)
    current_number_to = int(plants.acell(to_address_affected).value)
    print(f"{config.INDENT}You have chosen to hold back {current_cultivar} plants of age year-{affected_year}.\
    \n{config.INDENT}There are currently {current_number_from} plants of that category recorded in the system.\
    \n{config.INDENT}There are now {current_number_to} plants of that cultivar listed as being a year younger.\
    \n{config.INDENT}The specified number of plants will be held back for a year.")
    while True:
        number_held_back = input(f"{config.INDENT}How many plants of that category do you want to hold back a year? \n")
        try:
            number_held_back = int(number_held_back)
            if 0 <= number_held_back <= current_number_from:
                break
            else:
                print(f"{config.INDENT}You can't hold back more plants of this category than you actually have in the\
                \n{config.INDENT}nursery! Please enter an integer between 0 and {current_number_from}: ")
        except ValueError:
            print(f"{config.INDENT}Your number must be a positive integer or 0. Negative and decimal-point numbers,\
            \n{config.INDENT}text and special characters, etc. are not allowed: ")

    current_number_from -= number_held_back
    current_number_to += number_held_back
    plants.update_acell(from_address_affected, current_number_from)
    plants.update_acell(to_address_affected, current_number_to)
    print(f"{config.INDENT}Successfully recorded holding back {number_held_back} {current_cultivar} plants of year-{affected_year}.\
    \n{config.INDENT}You now have a remaining stock of {plants.acell(from_address_affected).value} plants of that category\
    \n{config.INDENT}and a total stock of {plants.acell(to_address_affected).value} of year-{affected_year - 1} plants of that cultivar.")

    print(f"{config.INDENT}Plants held back successfully.")

    print(f"{config.INDENT}Press Enter to continue ...")
    input('')


def bring_forward():
    """
    Option 9:
    The same as Option 9, but in the opposite direction.
    Results in the given number of cultivars from year n being removed
    and then added to year n+1.
    """

    # First define the cultivar affected
    row_values = plants.row_values(1)
    # Find the column to stop at (first column that contains no data).
    first_empty_index = next((i for i,
                              val in enumerate(row_values) if not val),
                             len(row_values))
    last_column = chr(ord('a') + first_empty_index)

    name_range = f"a1:{last_column}1"  # Names of cultivars
    cultivars = plants.get(name_range)[0]

    # List out the cultivars in the data in an ordered list.
    print(f"{config.INDENT}For which cultivar would you like bring plants forward?")
    list_cultivars(cultivars)

    cultivar_value = parse_user_input(input(f"{config.INDENT}Please enter the cultivar number for which you want to bring plants forward\
    \n{config.INDENT}(see the cultivars listed above): \n"))
    while True:
        affected_year = parse_user_input(input(f"{config.INDENT}Please enter the age of the plants for which you want to bring plants forward\
        \n{config.INDENT}(typing '1' for year-one plants or '2' for year-two plants, and so on): \n"))
        try:
            affected_year = int(affected_year)
            if affected_year >= 1:
                break
            else:
                print(f"{config.INDENT}Please enter an integer between 1 and the age of the nursery.")
        except ValueError:
            print(f"{config.INDENT}Your number must be an integer and must be at least 1, and less than the age of\
            \n{config.INDENT}the nursery. Negative and decimal-point numbers, text and special characters, etc.\
            \n{config.INDENT}are not allowed: ")

    from_address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 1}"
    to_address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 2}"

    current_cultivar = cultivars[cultivar_value - 1]
    current_number_from = int(plants.acell(from_address_affected).value)
    current_number_to = int(plants.acell(to_address_affected).value)
    print(f"{config.INDENT}You have chosen to bring forward {current_cultivar} plants of age year-{affected_year}.\
    \n{config.INDENT}There are currently {current_number_from} plants of that category recorded in the system.\
    \n{config.INDENT}There are now {current_number_to} plants of that cultivar listed as being a year older.\
    \n{config.INDENT}The specified number of plants will be brought forward by a year.")
    while True:
        number_brought_forward = input(f"{config.INDENT}How many plants of that category do you want to bring forward for a year? \n")
        try:
            number_brought_forward = int(number_brought_forward)
            if 0 <= number_brought_forward <= current_number_from:
                break
            else:
                print(f"{config.INDENT}You can't bring forward more plants of this category than you actually have in\
                \n{config.INDENT}the nursery!\
                \n{config.INDENT}Please enter an integer between 0 and {current_number_from}: ")
        except ValueError:
            print(f"{config.INDENT}Your number must be a positive integer or 0. Negative and decimal-point numbers,\
            \n{config.INDENT}text and special characters, etc. are not allowed: ")

    current_number_from -= number_brought_forward
    current_number_to += number_brought_forward
    plants.update_acell(from_address_affected, current_number_from)
    plants.update_acell(to_address_affected, current_number_to)
    print(f"{config.INDENT}Successfully recorded bringing forward {number_brought_forward} {current_cultivar} plants of year-{affected_year}.\
    \n{config.INDENT}You now have a remaining stock of {plants.acell(from_address_affected).value} plants of that category\
    \n{config.INDENT}and a total stock of {plants.acell(to_address_affected).value} of year-{affected_year + 1} plants of that cultivar.")

    print(f"{config.INDENT}Plants brought forward successfully.")

    print(f"{config.INDENT}Press Enter to continue ...")
    input('')


def create_year():
    """
    Option 0:
    This function adds the rows necessary to create a new year and copies the
    row for stocks of this year's grafts from the
    grafts-year-zero to the plants worksheet. It puts the current year out of
    reach of the relevant seasonal planning and work tasks.
    """
    rootstock_year = rootstock.acell('a2').value
    new_rootstock_year = int(rootstock_year) + 1

    print(f"{config.INDENT}The last year created was {rootstock_year}")
    cuttings_last_year = rootstock.acell('c3').value
    if input(f"{config.INDENT}Would you like to create a record for {new_rootstock_year}?\
    \n{input_texts.Y_OR_N_TEXT}\n").lower() == commands.YES:
        print(f"\n{config.INDENT}Info: You took {cuttings_taken} cuttings last year.\
        \n{config.INDENT}You now have {mature_rootstocks} maturing rootstocks in stock.")
        num_cuttings = parse_user_input(input(f"{config.INDENT}How many cuttings would you like to plan for {new_rootstock_year}? \
        \n{config.INDENT}(Enter 0 if you want to plan cutting numbers later): \n"))
        values = [new_rootstock_year, num_cuttings, 0, 0, 0]
        rootstock.insert_row(values, 2)
        rootstock.update_acell('e3', 0)
        print(msgs.year_created(new_rootstock_year, num_cuttings))
        if num_cuttings == 0:
            print(f"{config.INDENT}{msgs.CUTTINGS_LATER}")

        year_zero_stocks = grafts_year_zero.get('c4:h4')[0]

        year_zero_stocks_int = [int(value) for value in year_zero_stocks]
        plants.insert_rows([year_zero_stocks_int], 2)

        graft_starting_values = [
            [new_rootstock_year, 'planned', 0, 0, 0, 0, 0, 0, '=SUM(C2:H2)'],
            [new_rootstock_year, 'grafted', 0, 0, 0, 0, 0, 0, '=SUM(C3:H3)'],
            [new_rootstock_year, 'stock', 0, 0, 0, 0, 0, 0, '=SUM(C4:H4)'],
            [new_rootstock_year, 'lost', 0, 0, 0, 0, 0, 0, '=SUM(C5:H5)'],
            ]

        grafts_year_zero.insert_rows(graft_starting_values, 2)

        done_starting_values = [
            ['planning', 'n', '-','n','n','n','n','n', 'n', '=IF(COUNTIF(A2:I2, "y") = 7, "y","n")'],
            ['production', 'n', 'n','n','n','n','n','n', 'n', '=IF(COUNTIF(A3:I3, "y") = 8, "y","n")'],
        ]

        completed.overwrite_

    else:
        print(f"{config.INDENT}The year {new_rootstock_year} has not been created.\
        \n{config.INDENT}The current year is still {rootstock_year}")

    print(f"{config.INDENT}Press Enter to continue ...")
    input('')


"""
Program runs from here
"""
startup_instructions()
