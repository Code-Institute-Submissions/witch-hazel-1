import gspread
from google.oauth2.service_account import Credentials
import sys


help_text1 = "\n##########################################################################\
    \n\n                             W I T C H - H A Z E L\
    \n\nTo run witch-hazel, call the script file that contains its code\
    \nby simply typing the name of the file on the command line (``run.py``).\
    \nOn opening, the app will show you a list of the options available to\
    \nyou and ask which of them you would like to perform.\
    \n\n0. Help\
    \n1. Close out current year\
    \n\n2. Plan this year's cutting campaign\
    \n3. Record cuttings taken\
    \n4. Record rooted cuttings potted up\
    \n\n5. Plan grafts for this year\
    \n\n6. Record grafts taken\
    \n\n7. Record plant losses\
    \n8. Record plant gains\
    \n9. Hold plants over for one year\
    \n10. Bring plants forward one year\
    \n\n11. Add new cultivar"

help_text2 = "Type the number of the operation you wish to perform.\
    \nThe app will guide you through the operation you have chosen to perform.\
    \nYou will need to restart the app each time you wish to run an operation.\
    \n\nLook at the README.md file for details on each of these options.\
    \n\nIn places it may need to ask you a yes or no question. Where this\
    \nhappens you should answer yes by typing a 'y' or 'Y' on the\
    \ncommand line. Typing in any other symbol will be taken as a 'No', and\
    \nwill result in the app closing.\
    \n\nIn other cases you'll be asked to enter a number. It will usually\
    \nindicate the valid range. Negative numbers are always taken as\
    \n invalid. Any time you enter an invalid number, the app will give you\
    \n another opportunity to enter a valid one.\
    \nEntering a non-numerical character where a number is expected will\
    \ncause the program to exit.\
    \n\n\nPlease look at the relevant section of the README.md file to find\
    \nout which numbers are valid in each individual user interaction.\
    \n\n###############################################################################\
    \n"

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

cuttings_taken = int(rootstock.acell('c1').value)
rootstocks_potted = int(rootstock.acell('d1').value)
mature_rootstocks = int(rootstock.acell('e1').value)

rootstock_data = rootstock.get_all_values()
grafts_data = grafts_year_zero.get_all_values()
Plants_data = plants.get_all_values()

def check_is_numeric(user_input, min=0, max=10000, not_a_number_blurb=" is not a number. Please enter a number between ", 
        not_in_range_blurb="That number is out of range. Please enter a number between "):
    try:
        number = int(user_input)
        if min <= number <= max:
            return number
        else:
            return check_is_numeric(input(f"{not_in_range_blurb}{min} and {max}:"), min, max)
    except:
        if user_input.lower()=='exit':
            exit()
        else:
            return check_is_numeric(input(f"{user_input}{not_a_number_blurb}{min} and {max}:"), min, max)

def Get_survival_rate(start_num, end_num):
    if int(start_num) == 0:
        return 'The starting number is not recorded.'
    elif int(end_num) > int(start_num):
        return 'You ended up with more units than you started with.'
    else:
        return int(end_num) / int(start_num)

cutting_success = Get_survival_rate(cuttings_taken, rootstocks_potted)
potting_success = Get_survival_rate(rootstocks_potted, mature_rootstocks)


def Startup_instructions():
    """
    The program's main menu on startup
    The user may need to scroll up to see the whole text.
    """

    Intro_text1 = "**************************************************************\
    \n\
    \nWelcome to witch-hazel, your simple app for planning your production of\
    \ngrafted Hamamelis plants!\
    \n\
    \n\
    \nFor a full list of the program's functions and instructions on how\
    \nto call them, enter '0' on the command line. This will show you\
    \n the HELP text for the app.\
    \n\nType 'EXIT' to close the witch-hazel app.\
    \n\
    \n_____________________________________________________________________________"

    Intro_text2 = "\n\
    \nWhat would you like to do?\
    \nChoose from among the following operations:\
    \n\n0. Help\
    \n\n1. Create new year/Close out current year\
    \n\n2. Plan this year's cutting campaign\
    \n3. Record cuttings taken\
    \n4. Record rooted cuttings potted up\
    \n\n5. Plan grafts for this year\
    \n6. Record grafts taken\
    \n\n7. Record plant losses\
    \n8. Record plant gains\
    \n9. Hold over plants for one year\
    \n10. Bring plants forward one year\
    \n\n11. Add new cultivar\
    \n"

    lower_bound = 0
    upper_bound = 11

    print(Intro_text1)
    print("Press Enter to continue ...")
    input()
    print(Intro_text2)

    while True:
        user_input = input(f"Please indicate which operation you would like to perform by\
        \nentering the corresponding number: \n")
        try:
            int_option = int(user_input)
            if lower_bound <= int_option <= upper_bound:
                break
            else:
                print(f"Invalid input. Your number must be a whole number between {lower_bound} and\
                \n{upper_bound}. Please enter a valid number: ")
        except ValueError:
            if user_input.lower() == 'exit':
                print("Exiting witch-hazel app")
                exit()
            else:
                print(f"Your number must be a positive integer or 0. Negative and\
                \ndecimal-point numbers, text and special characters, etc. are not allowed:\n")

    Execute_option(int_option)


def Help():
    """
    Option 0
    """
    print(help_text1)
    input("Press Enter to see more help!")
    print(help_text2)

    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Create_year():
    """
    Option 1:
    This function adds the rows necessary to create a new year and copies the
    row for stocks of this year's grafts from the
    grafts-year-zero to the plants worksheet. It puts the current year out of
    reach of the relevant seasonal planning and work tasks.
    """
    rootstock_year = rootstock.acell('a1').value
    new_rootstock_year = int(rootstock_year) + 1

    print(f"The last year created was {rootstock_year}")
    cuttings_last_year = rootstock.acell('c2').value
    if input(f"Would you like to create a record for {new_rootstock_year}?\
    \nType 'y' for yes and 'n' for no: \n").lower() == 'y':
        print(f"\nInfo: You took {cuttings_taken} cuttings last year.\
        \nYou now have {mature_rootstocks} maturing rootstocks in stock.")
        num_cuttings = check_is_numeric(input(f"How many cuttings would you like to plan for {new_rootstock_year}? \
        \n(Enter 0 if you want to plan cutting numbers later): \n"))
        values = [new_rootstock_year, num_cuttings, 0, 0, 0]
        rootstock.insert_row(values)
        rootstock.update_acell('e3', 0)
        print(f"Year {new_rootstock_year} created. {num_cuttings} cuttings planned\
        \nfor this year.")
        if num_cuttings == 0:
            print("You've chosen to plan your cutting campaign later!")

        year_zero_stocks = grafts_year_zero.get('c4:h4')[0]

        year_zero_stocks_int = [int(value) for value in year_zero_stocks]
        plants.insert_rows([year_zero_stocks_int], 2)

        graft_starting_values = [
            [new_rootstock_year, 'planned', 0, 0, 0, 0, 0, 0],
            [new_rootstock_year, 'grafted', 0, 0, 0, 0, 0, 0],
            [new_rootstock_year, 'stock', 0, 0, 0, 0, 0, 0],
            ]

        grafts_year_zero.insert_rows(graft_starting_values, 2)

    else:
        print(f"The year {new_rootstock_year} has not been created.\
        \nThe current year is still {rootstock_year}")

    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Plan_cutting_campaign():
    """
    Option 2:
    Helps plan cuttings task
    """
    planned_cuttings = int(rootstock.acell('b1').value)
    last_year_cuttings = int(rootstock.acell('c2').value)
    last_year_rooted_cuttings = int(rootstock.acell('d2').value)
    this_year_cuttings_taken = int(rootstock.acell('c1').value)
    current_year = int(rootstock.acell('a1').value)
    if int(planned_cuttings) > 0:
        if input(f"So far you have planned to take {planned_cuttings} cuttings for {current_year}! Would you like replace that number with a new one?\
        \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
            
            planned_cuttings = check_is_numeric(input(f"You took {last_year_cuttings} cuttings last year, resulting in {last_year_rooted_cuttings} successfully rooted cuttings.\
            \nThe present planned figure for this year is {planned_cuttings}.\
            \nEnter a new figure for planned cuttings for this year: \n"))
            if planned_cuttings <= this_year_cuttings_taken:
                if input(f"You have already taken {this_year_cuttings_taken} cuttings this year. This is more than your new planned figure!\
                \nAre you sure you want to replace the planned figure with this one?\
                \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
                    rootstock.update_acell('b1', planned_cuttings)
                    print("Planned number of cuttings successfully changed.\
                    \nCuttings campaign planning session completed")
            else:
                rootstock.update_acell('b1', planned_cuttings)
                print("Planned number of cuttings successfully changed.\
                \nCuttings campaign planning session completed")
        else:
            print("Plan cuttings action cancelled.\
            \nNo changes have been made to the data.")
    else:
        if input(f"Would you like to plan the number of cuttings you intend to take this season? \
        \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
            planned_cuttings = check_is_numeric(input(f"Please enter the number of cuttings\
            \nthat you want to take this year: \n"))
            rootstock.update_acell('b1', planned_cuttings)
            print("Planned number of cuttings successfully changed.\
            \nCuttings campaign planning session completed")
        else:
            print("Plan cuttings action cancelled.\
            \nNo changes have been made to the data.")

    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Run_main_if_clause(taken, planned):
    """
    Option 3:
    Lets user record cuttings.
    Ideally used daily during the cuttings campaign (in Autumn).
    """
    if taken >= planned:
        print(f"You have already reached the number of cuttings you planned to take this year: \
        \n{taken} cuttings taken out of {planned} planned!")
    else:
        print(f"So far you have taken {taken} cuttings!")

    if input("Would you like to add to that number?\
    \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
        taken += check_is_numeric(input(f"How many cuttings have you now taken in addition to the ones\
        \nyou've already recorded: \n"))
        rootstock.update_acell('c1', taken)
        if taken >= planned:
            print(f"Congratulations! You have achieved the planned number of cuttings: \
            \n{taken} cuttings taken out of {planned} planned!")
        else:
            print(f"You have now taken a total of {taken} cuttings out of a planned total\
            \nof {planned}!")

        print("Cuttings campaign record added successfully.")
    else:
        print("Cuttings taken action cancelled.\
        \nNo changes have been made to the data.")
    
    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Record_cuttings_taken():
    cuttings_taken = int(rootstock.acell('c1').value)
    cuttings_planned = int(rootstock.acell('b1').value)
    cuttings_rooted = int(rootstock.acell('d1').value)
    if cuttings_rooted > 0:
        if input("You have already begun potting up cuttings for this year.\
        \nAre you sure you want to take cuttings at this time?\
        \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
            Run_main_if_clause(cuttings_taken, cuttings_planned)
        else:
            print("Record new cuttings taken action cancelled.\
            \nNo changes have been made to the data.")
    else:
        Run_main_if_clause(cuttings_taken, cuttings_planned)

    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Record_potted_cuttings():
    """
    Option 4:
    Lets user record progress in potting up the successfully rooted cuttings
    (taken the previous Autumn).
    Ideally used daily during the potting campaign (in the Spring).
    """
    cuttings_taken = int(rootstock.acell('c1').value)
    cuttings_potted = int(rootstock.acell('d1').value)
    new_rootstocks = int(rootstock.acell('e1').value)
    if input(f"So far you have potted up {cuttings_potted} cuttings! Would you like to add to that number?\
    \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
        newly_potted = check_is_numeric(input(f"How many cuttings have you now potted up in addition\
        \nto the ones already recorded: \n"))
        if cuttings_potted + newly_potted > cuttings_taken:
            print(f"If {newly_potted} is added to the existing figure of newly rooted cuttings ({new_rootstocks}), then you'll have potted up more cuttings than you took in the Autumn.\
            \nThat is not normally possible!\
            \nIf you're sure that the total number of newly potted rootstocks is in fact {newly_potted + new_rootstocks}, \
            \nthen you must first change the figure for cuttings (Option 3) before continuing!\
            \nRecord new cuttings potted action cancelled.\
            \nNo changes have been made to the data.")
        else:
            cuttings_potted += newly_potted
            new_rootstocks += newly_potted
            rootstock.update_acell('d1', cuttings_potted)
            rootstock.update_acell('e1', new_rootstocks)
            print(f"You have now potted up a total of {cuttings_potted} cuttings out of a total of {cuttings_taken}!\
            \nThat means you now have {new_rootstocks} immature rootstocks available for grafting next year\
            \n(minus any losses in the meantime).")
    else:
        print("Record new cuttings potted action cancelled.\
        \nNo changes have been made to the data.")

    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Plan_grafting_campaign():
    """
    Option 5:
    Lets user add a planned number of grafts for each cultivar.
    Should be used in late winter (February or March).
    Shows the number of rootstocks ready for grafting and the number left.
    Warns the user when they're planning to use more rootstocks than they have.
    """
    rootstocks_available = int(rootstock.acell('e2').value)

    row_values = grafts_year_zero.row_values(1)
    # Find the column to stop at (first column that contains no data)
    first_empty_index = next((i for i,
                              val in enumerate(row_values) if not val),
                             len(row_values))
    last_column = chr(ord('a') + first_empty_index)

    name_range = f"c1:{last_column}1"
    planned_range = f"c2:{last_column}2"

    cultivars = grafts_year_zero.get(name_range)[0]
    planned_numbers = grafts_year_zero.get(planned_range)[0]
    """
    Converts the strings in the planned numbers list into integers
    to make it possible to sum them together.
    """
    planned_numbers = [int(x) for x in planned_numbers]
    total_planned = sum(planned_numbers)

    print(f"For which cultivar would you like to plan a grafting campaign?\
    \nYou currently have {rootstocks_available} rootstocks available for use in grafting.\
    \nOf these, {rootstocks_available - total_planned} are not yet\
    \nreserved in your plan")

    # List out the cultivars you have in your data in an ordered list.
    count = 0
    for cultivar in cultivars:
        count += 1
        print(f"{count}. {cultivar}")

    print("For which cultivar would you like to plan your grafting?\n")
    cultivar_value = check_is_numeric(input("Please enter the number of the cultivar for which you want to plan grafting\
    \n(see the cultivars listed above): \n"), 1, count)
    cell_address = f"{chr(ord('c') + cultivar_value - 1)}2"
    print(cell_address)
    print(f"You have chosen to plan graft numbers\
    \nfor {cultivars[cultivar_value - 1]}")
    print(f"So far, you have planned to make\
    \n{planned_numbers[cultivar_value - 1]} grafts of this cultivar.")
    if input("Would you like to replace this value?\
    \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
        new_planned_value = check_is_numeric(input(f"Type in the new planned value\
        \nfor {cultivars[cultivar_value - 1]}: \n"))
        grafts_year_zero.update_acell(cell_address, new_planned_value)
        print(f"Planned number of grafts for {cultivars[cultivar_value - 1]} successfully changed.\
            \nCuttings campaign planning session completed")

    else:
        print(f"Plan grafts action for {cultivars[cultivar_value - 1]} cancelled.\
        \nNo changes have been made to the data.")
    
    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Record_grafts():
    """
    Option 6:
    Lets user record the number of grafts taken for a chosen cultivar.
    Should be used in late winter; at grafting time.
    Shows the total for rootstocks ready for grafting and the number left.
    Warns the user when they've used more rootstocks than they actually have.
    """
    rootstocks_available = int(rootstock.acell('e2').value)

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
    total_planned = sum(planned_numbers)
    grafts_this_year = grafts_year_zero.get(grafted_range)[0]
    grafts_this_year = [int(x) for x in grafts_this_year]
    total_grafted = sum(grafts_this_year)

    print(f"For which cultivar would you like record new grafts completed?\
    \nYou currently have {rootstocks_available} rootstocks available for use in grafting.\
    \nOf these, {rootstocks_available - total_planned} are not yet reserved\
    \nin your plan.")

    # List out the names of the cultivars you have in your data
    # in an ordered list.
    count = 0
    for cultivar in cultivars:
        count += 1
        print(f"{count}. {cultivar}")

    print("Which cultivar has been grafted?\n")

    cultivar_value = check_is_numeric(input("Please enter the cultivar number of the new grafts you want to record\
    \n(see the cultivars listed above): \n"), 1, count)
    address_grafts = f"{chr(ord('c') + cultivar_value - 1)}3"
    address_rootstocks = 'e2'
    grafts_this_cultivar = grafts_this_year[cultivar_value - 1]
    print(f"You have chosen to record grafts of\
    \n{cultivars[cultivar_value - 1]}")
    print(f"So far, you have grafted {grafts_this_cultivar} of this cultivar.")
    if input("Would you like to add to this value?\
    \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
        newly_made_grafts = check_is_numeric(input(f"Type in the number of new grafts you have made of\
        \n{cultivars[cultivar_value - 1]}: \n"))
        grafts_this_cultivar += newly_made_grafts
        grafts_year_zero.update_acell(address_grafts, grafts_this_cultivar)
        rootstock.update_acell(address_rootstocks,
                               int(rootstock.acell(address_rootstocks).value) -
                               newly_made_grafts)
        print(f"Number of grafts made for {cultivars[cultivar_value - 1]} successfully changed.\
            \nThe new total of grafts made this year\
            \nfor this cultivar is {grafts_year_zero.acell(address_grafts).value}\
            \nSuccessfully completed record of new grafts made.")

    else:
        print(f"Plan grafts action for {cultivars[cultivar_value - 1]} cancelled.\
        \nNo changes have been made to the data.")
    
    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Record_loss():
    """
    Option 7:
    Lets user record losses in stocks for any cultivar in any year.
    Works for both rooted cuttings and grafted cultivars.
    May be used throughout the year.
    Losses of cuttings are not recorded until the time comes to pot
    up those of them that have rooted successfully.
    """
    # Did we lose new_rootstocks?
    if input(f"Would you like to record a loss of new rootstocks?\
    \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
        address_affected = 'e1'
        total_rootstocks = int(rootstock.acell(address_affected).value)

        print(f"At the last count there were {total_rootstocks} new rootstocks in the nursery")

        while True:
            number_lost = input("How many rootstocks have been lost since then? \n")
            try:
                number_lost = int(number_lost)
                if 0 <= number_lost <= total_rootstocks:
                    break
                else:
                    print(f"You can't have lost more rootstocks than you actually had in the nursery!\
                    \nPlease enter an integer between 0 and\
                    {total_rootstocks}: ")
            except ValueError:
                print(f"Your number must be a positive integer or 0. Negative and decimal-point numbers,\
                \ntext and special characters, etc. are not allowed: ")

        rootstock.update_acell(address_affected,
                               total_rootstocks - number_lost)
        print(f"Loss of {number_lost} new rootstocks recorded.\
        \nYou now have a stock of {rootstock.acell(address_affected).value} new rootstocks.")
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
        print(f"For which cultivar would you like record a loss?")
        count = 0
        for cultivar in cultivars:
            count += 1
            print(f"{count}. {cultivar}")

        cultivar_value = check_is_numeric(input("Please enter the cultivar number for which you want to record a loss\
        \n(see the cultivars listed above): \n"))
        affected_year = check_is_numeric(input("Please enter the age of the plants for which you want to record a loss\
        \n(typing '1' for year-one plants, '2' for year-two plants, and so on): \n"))
        address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 1}"

        current_number = int(plants.acell(address_affected).value)
        print(f"You have chosen to register a loss of {cultivars[cultivar_value - 1]} of age year-{affected_year}.\
        \nThere are currently {current_number} plants of that category\
        recorded in the system.")
        while True:
            number_lost = input("How many plants of that category have been lost since then? \n")
            try:
                number_lost = int(number_lost)
                if 0 <= number_lost <= current_number:
                    break
                else:
                    print(f"You can't have lost more plants of this category than you actually had in the nursery!\
                    \nPlease enter an integer between 0 and {current_number}.")
            except ValueError:
                print(f"Your number must be a positive integer or 0.\
                \nNegative and decimal-point numbers, text and special characters, etc. \
                are not allowed: ")
        current_number -= number_lost
        plants.update_acell(address_affected, current_number)
        print(f"Loss of {number_lost} {cultivars[cultivar_value - 1]} of year-{affected_year} recorded.\
        \nYou now have a remaining stock of {plants.acell(address_affected).value} plants of that category.")

        # number_lost
    print("Loss recorded successfully.")

    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Record_gain():
    """
    Option 8:
    Essentially the opposite of Option 7.
    """
    # Did we acquire new_rootstocks ...?
    if input(f"Would you like to record an acquisition of new rootstocks?\
    \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
        address_affected = 'e1'
        total_rootstocks = int(rootstock.acell(address_affected).value)

        print(f"At the last count there were {total_rootstocks} \
        new rootstocks in the nursery")

        while True:
            number_gained = input("How many rootstocks have\
            been acquired since then? \n")
            try:
                number_gained = int(number_gained)
                break
            except ValueError:
                print(f"Your number must be a positive integer or 0.\
                \nNegative and decimal-point numbers, text and special characters, \
                etc. are not allowed: ")

        rootstock.update_acell(address_affected,
                               total_rootstocks + number_gained)
        print(f"Acquisition of {number_gained} new rootstocks recorded.\
        \nYou now have a stock of {rootstock.acell(address_affected).value}\
        new rootstocks.")
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
        print(f"For which cultivar would you like record an acquisition?")
        count = 0
        for cultivar in cultivars:
            count += 1
            print(f"{count}. {cultivar}")

        cultivar_value = check_is_numeric(input("Please enter the cultivar number for which you want to enter an acquisition\
        \n(see the cultivars listed above): \n"), 1, count)
        affected_year = check_is_numeric(input("Please enter the age of the plants for which you want to enter an acquisition\
        \n(typing '1' for year-one plants, '2' for year-two plants, and so on): \n"), 1, 5)
        address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 1}"

        current_number = int(plants.acell(address_affected).value)
        print(f"You have chosen to register an acquisition of {cultivars[cultivar_value - 1]} of age year-{affected_year}.\
        \nThere are currently {current_number} plants of that category recorded in the system.")
        while True:
            number_gained = input("How many plants of that category have been acquired since the last recorded entry? \n")
            try:
                number_gained = int(number_gained)
                break
            except ValueError:
                print(f"Your number must be a positive integer or 0.\
                \nNegative and decimal-point numbers, text and special characters, etc. \
                are not allowed: ")
        current_number += number_gained
        plants.update_acell(address_affected, current_number)
        print(f"Acquisition of {number_gained} {cultivars[cultivar_value - 1]} of year-{affected_year} recorded.\
        \nYou currently have a stock of {plants.acell(address_affected).value} plants of that category.")

        # number_lost
    print("Acquisition recorded successfully.")
    
    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Hold_back():
    """
    Option 9:
    Essentially a Option 7 with a twist.
    Results in the given number of the chosen cultivar from year n
    being removed and then added to year n-1.
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
    print(f"For which cultivar would you like hold back plants?")
    count = 0
    for cultivar in cultivars:
        count += 1
        print(f"{count}. {cultivar}")

    cultivar_value = check_is_numeric(input("Please enter the cultivar number for which you want to hold plants back (see\
    \nthe cultivars listed above): \n"))
    while True:
        affected_year = check_is_numeric(input("Please enter the age of the plants that you want to hold back (typing '2'\
        \nfor year-two plants or '3' for year-three plants, and so on): \n"))
        try:
            affected_year = int(affected_year)
            if affected_year > 1:
                break
            elif affected_year == 1:
                print(f"Year-one plants cannot be held back. Enter 2 or higher. But remember there's\
                \nno point in entering an age greater than the age of the \
                nursery.")
            else:
                print(f"Please enter an integer between 2 and \
                the age of the nursery.")
        except ValueError:
            print(f"Your number must be an integer greater than 2 and less than the age of the\
            \nnursery. Negative and decimal-point numbers, text and special characters, etc.\
            \nare not allowed: ")

    from_address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 1}"
    to_address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year}"

    current_number_from = int(plants.acell(from_address_affected).value)
    current_number_to = int(plants.acell(to_address_affected).value)
    print(f"You have chosen to hold back {cultivars[cultivar_value - 1]} plants of age year-{affected_year}.\
    \nThere are currently {current_number_from} plants of that category recorded in the system.\
    \nThere are now {current_number_to} plants of that cultivar listed as being a year younger.\
    \nThe specified number of plants will be held back for a year.")
    while True:
        number_held_back = input("How many plants of that category do you want to hold back a year? \n")
        try:
            number_held_back = int(number_held_back)
            if 0 <= number_held_back <= current_number_from:
                break
            else:
                print(f"You can't hold back more plants of this category than you actually have in the\
                \nnursery! Please enter an integer between 0 and \
                {current_number_from}: ")
        except ValueError:
            print(f"Your number must be a positive integer or 0. Negative and decimal-point numbers,\
            \ntext and special characters, etc. are not allowed: ")

    current_number_from -= number_held_back
    current_number_to += number_held_back
    plants.update_acell(from_address_affected, current_number_from)
    plants.update_acell(to_address_affected, current_number_to)
    print(f"Successfully recorded holding back {number_held_back} {cultivars[cultivar_value - 1]} plants of year-{affected_year}.\
    \nYou now have a remaining stock of {plants.acell(from_address_affected).value} plants of that category\
    \nand a total stock of {plants.acell(to_address_affected).value} of year-{affected_year - 1} plants of that cultivar.")

    print("Plants held back successfully.")

    print("Press )any key to continue ...")
    input()
    Startup_instructions()


def Bring_forward():
    """
    Option 10:
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
    print(f"For which cultivar would you like bring plants forward?")
    count = 0
    for cultivar in cultivars:
        count += 1
        print(f"{count}. {cultivar}")

    cultivar_value = check_is_numeric(input("Please enter the cultivar number for which you want to bring plants forward\
    \n(see the cultivars listed above): \n"))
    while True:
        affected_year = check_is_numeric(input("Please enter the age of the plants for which you want to bring plants forward\
        \n(typing '1' for year-one plants or '2' for year-two plants, and so on): \n"))
        try:
            affected_year = int(affected_year)
            if affected_year >= 1:
                break
            else:
                print(f"Please enter an integer between 1 and the \
                age of the nursery.")
        except ValueError:
            print(f"Your number must be an integer and must be at least 1, and less than the age of\
            \nthe nursery. Negative and decimal-point numbers, text and special characters, etc.\
            \nare not allowed: ")

    from_address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 1}"
    to_address_affected = f"{chr(ord('a') + cultivar_value - 1)}{affected_year + 2}"

    current_number_from = int(plants.acell(from_address_affected).value)
    current_number_to = int(plants.acell(to_address_affected).value)
    print(f"You have chosen to bring forward {cultivars[cultivar_value - 1]} plants of age year-{affected_year}.\
    \nThere are currently {current_number_from} plants of that category recorded in the system.\
    \nThere are now {current_number_to} plants of that cultivar listed as being a year older.\
    \nThe specified number of plants will be brought forward by a year.")
    while True:
        number_brought_forward = input("How many plants of that category do you want to bring forward for a year? \n")
        try:
            number_brought_forward = int(number_brought_forward)
            if 0 <= number_brought_forward <= current_number_from:
                break
            else:
                print(f"You can't bring forward more plants of this category than you actually have in\
                the nursery!\
                \nPlease enter an integer between 0 and \
                {current_number_from}: ")
        except ValueError:
            print(f"Your number must be a positive integer or 0. Negative and decimal-point numbers,\
            \ntext and special characters, etc. are not allowed: ")

    current_number_from -= number_brought_forward
    current_number_to += number_brought_forward
    plants.update_acell(from_address_affected, current_number_from)
    plants.update_acell(to_address_affected, current_number_to)
    print(f"Successfully recorded bringing forward {number_brought_forward} {cultivars[cultivar_value - 1]} plants of year-{affected_year}.\
    \nYou now have a remaining stock of {plants.acell(from_address_affected).value} plants of that category\
    \nand a total stock of {plants.acell(to_address_affected).value} of year-{affected_year + 1} plants of that cultivar.")

    print("Plants brought forward successfully.")

    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Add_new_cultivar():
    """
    Option 11:
    Adds new cultivar to the list of Hamamelis plants grown in the nursery.
    """
    print("This functionality has not yet been implemented.\
    \nPlease watch this space!")

    print("Press Enter to continue ...")
    input()
    Startup_instructions()


def Execute_option(operation):
    """
    Executes the option chosen by the user
    """

    print("_____________________________________________________________________________")
    print(" ")
    if operation == 0:
        print("You've chosen HELP.")
        Help()
    elif operation == 1:
        print("You've chosen to close out the current year and open a new one.")
        Create_year()
    elif operation == 2:
        print("You've chosen to plan this year's cutting campaign.")
        Plan_cutting_campaign()
    elif operation == 3:
        print("You've chosen to record having taken some cuttings.")
        Record_cuttings_taken()
    elif operation == 4:
        print("You've chosen to record potting up some rooted cuttings.")
        Record_potted_cuttings()
    elif operation == 5:
        print("You've chosen to plan your grafting campaign.")
        Plan_grafting_campaign()
    elif operation == 6:
        print("You've chosen to record a number of new grafts.")
        Record_grafts()
    elif operation == 7:
        print("You've chosen to record the loss of a number of plants.")
        Record_loss()
    elif operation == 8:
        print("You've chosen to record the acquisition of a number of plants.")
        Record_gain()
    elif operation == 9:
        print("You've chosen to hold a number of grafted plants back a year.")
        Hold_back()
    elif operation == 10:
        print("You've chosen to bring a number of grafted plants forward a year.")
        Bring_forward()
    elif operation == 11:
        print("Sorry! This functionality has not yet been implemented.")
        Add_new_cultivar()
    else:
        print("Please enter a valid integer between 0 (for Help) and 11")


Startup_instructions()
