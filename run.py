import gspread
from google.oauth2.service_account import Credentials
import sys

startup_instructions = "You must enter an argument after the program script name to use this program.\
    \nSimply entering 'run.py' on the command line is not enough.\
    \nYou must enter a command in the form 'run.py nnnn' (where 'nnnn' is the name of one of the functions that the program contains).\
    \nFor a full list of the program's functions and instructions on how to call them, enter 'run.py help' on the command line.\
    \nAlways be careful to use only lower case letters."

help_text = "\n#############################################################################################################################################################\
    \n                                                         W I T C H  H A Z E L\
    \n\nTo run Witch Hazel from the command line you need to call the script file that contains its code ('run.py') followed by a space, followed by the name of the operation\
    \nyou want to execute.\
    \nPlease enter one of the operations available using exactly the spelling shown below, and remembering that the names are case-sensitive.\
    \nFor example, if you want to plan your cutting production for the year, carefully type 'run.py plan_cuttings' on the command line.\
    \n\nThe following is a list of the operations that this program can help you execute:\
    \n\n    help:          The 'help' operation produces this information message. It shows you how to use this program. \
    \n\n    new_year:      Creates a new year (it should be run once in the autumn of the previous year).\
    \n                   Once you have created your new new year, you will be asked if you want to plan your cuttings and/or grafts for that year immediately.\
    \n                   If you are not ready to plan all your cuttings or grafting, you can leave all or part of that task until later, by calling the 'plan_cuttings' or\
    \n                   'plan_grafting' operations later.\
    \n\n    plan_cuttings: This operation asks you to enter the number of cuttings you wish to produced of your currently preferred rootstock.\
    \n\n    take_cuttings: This operation asks you how many cuttings you want to add to the record of cuttings actually taken. It tots up a running total.\
    \n\n    pot_cuttings: This operation asks you how many successfully rooted cuttings you want to add to the record of potted up grafts. It tots a running total.\
    \n\n    plan_grafting: This operation first asks you to choose the cultivar for which you wish to produce grafts.\
    \n                   It then asks you to enter the number of grafts you wish to produce, giving you the information on how many root stocks are currently available.\
    \n\n    record_loss:   This operation asks you to choose the cultivar and age of the plants for which you want to record a loss.\
    \n                   It then asks you how many plants of that cultivar and age you have lost.\
    \n\n    record_gain:   This operation asks you to choose the cultivar and age of the plants for which you want to record an acquisition or other gain.\
    \n                   It then asks you how many plants of that cultivar and age you have gained or acquired.\
    \n\n    check_stock: This operation asks to choose a cultivar and age and shows you how many of that plant you have in stock, and how many\
    \n                   of them you originally grafted in year zero. It also shows a percentage loss rate since year zero.\
    \n\n    hold_back:     This operation asks you to choose the cultivar whose age distribution numbers you wish to adjust and the affected age.\
    \n                   It then asks you how many plants of that cultivar and age you wish to hold back for one year. It is identical to recording a loss for\
    \n                   the cultivar and age you have chosen and then recording a gain for the plants of that cultivar one year younger.\
    \n\n    bring_forward: This operation asks you to choose the cultivar whose age distribution numbers you wish to adjust and the affected age.\
    \n                   It then asks you how many plants of that cultivar and age you wish to bring forward by one year. It is identical to recording a loss for\
    \n                   the cultivar and age you have chosen and then recording a gain for the plants of that cultivar one year older.\
    \n\n#############################################################################################################################################################\
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


def Get_survival_rate(start_num, end_num):
    if int(start_num) == 0:
        return 'The starting number is not recorded.'
    elif int(end_num) > int(start_num):
        return 'You ended up with more units than you started with.'
    else:
        return int(end_num) / int(start_num)

def Is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def Plan_grafts(graft_num):
    column_letter = chr(ord('C') + graft_num - 1)
    
    cultivar_name_address = f"{column_letter}1"
    cell_address = f"{column_letter}2"
    cultivar_name = grafts_year_zero.acell(cultivar_name_address).value
    current_value = int(grafts_year_zero.acell(cell_address).value)
    print(f"The current planned figure you have for this year for {cultivar_name} is {current_value}. \n\n ")
    new_value = int(input("What value would you like to replace that number with? \n "))
    grafts_year_zero.update_acell(cell_address, value)1
    jaime

cutting_success = Get_survival_rate(cuttings_taken, rootstocks_potted) 
potting_success = Get_survival_rate(rootstocks_potted, mature_rootstocks)

rootstock_data = rootstock.get_all_values()
print(rootstock_data)

def Startup_instructions():
    print(startup_instructions)

def Create_year():
    rootstock_year = rootstock.acell('a1').value
    new_rootstock_year = int(rootstock_year) + 1

    print(f"The last year created was {rootstock_year}")
    cuttings_last_year = rootstock.acell('c2').value
    if input(f"Would you like to create a record for {new_rootstock_year}? Type 'y' for yes and 'n' for no: \n").lower() == 'y':
        print(f"\nInfo: You took {cuttings_taken} cuttings last year and successfully potted {rootstocks_potted} ({round(cutting_success * 100)}%) of them.\
        \nYou currently have {mature_rootstocks} maturing rootstocks in stock.")
        num_cuttings = int(input(f"How many cuttings would you like to plan for {new_rootstock_year}? \
        \n(Enter 0 if you would like to plan the number of cuttings to be taken later): \n"))
        values = [new_rootstock_year, num_cuttings, 0, 0, 0]
        rootstock.insert_row(values)  
        print(f"Year {new_rootstock_year} created. {num_cuttings} cuttings planned for this year.")
        if num_cuttings == 0:
            print("You've chosen to plan your cutting campaign later!")
        
        year_zero_stocks = grafts_year_zero.get('c4:h4') [0]

        year_zero_stocks_int = [int(value) for value in year_zero_stocks]
        plants.insert_rows([year_zero_stocks_int], 2)

        graft_starting_values = [
            [new_rootstock_year, 'planned', 0, 0, 0, 0, 0, 0],
            [new_rootstock_year, 'grafted', 0, 0, 0, 0, 0, 0],
            [new_rootstock_year, 'stock', 0, 0, 0, 0, 0, 0],
            ]

        grafts_year_zero.insert_rows(graft_starting_values, 2)

    else:
        print(f"The year {new_rootstock_year} has not been created. The current year is still {rootstock_year}")

def Plan_cutting_campaign():
    planned_cuttings = rootstock.acell('b1').value
    last_year_cuttings = rootstock.acell('c2').value
    if int(planned_cuttings) > 0:
        if input(f"So far you have planned to take {planned_cuttings} cuttings! Would you like replace that number with a new one?\
        \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
            planned_cuttings = int(input(f"You took {last_year_cuttings} cuttings last year. The present planned figure for this year is {planned_cuttings}. Please enter a new figure for planned cuttings for this year: \n"))
            rootstock.update_acell('b1', planned_cuttings)
            print("Cuttings campaign planning session completed")
        else:
            Print("Plan cuttings action cancelled.")
    else:
        if input(f"Would you like to plan the number of cuttings you intend to take this season? \
        \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
            planned_cuttings = int(input(f"Please enter the number of cuttings you want to take this year: \n"))
            rootstock.update_acell('b1', planned_cuttings)
            print("Cuttings campaign planning session completed")
        else:
            Print("Plan cuttings action cancelled.")

def Record_cuttings_taken():
    cuttings_taken = int(rootstock.acell('c1').value)
    cuttings_planned = int(rootstock.acell('b1').value)
    if input(f"So far you have taken {cuttings_taken} cuttings! Would you like to add to that number?\
        \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
        cuttings_taken += int(input(f"How many cuttings have you now taken in addition to the ones already recorded: \n"))
        rootstock.update_acell('c1', cuttings_taken)
        print(f"You have now taken a total of {cuttings_taken} cuttings out of a planned_total of {cuttings_planned}!")
    else:
        print("Record new cuttings taken action cancelled.")

def Record_potted_cuttings():
    cuttings_taken = int(rootstock.acell('c1').value)
    cuttings_potted = int(rootstock.acell('d1').value)
    new_rootstocks = int(rootstock.acell('e1').value)
    if input(f"So far you have taken {cuttings_taken} cuttings! Would you like to add to that number?\
        \nType 'y' for yes or 'n' for no: \n").lower() == 'y':
        newly_potted = int(input(f"How many cuttings have you now potted up in addition to the ones already recorded: \n"))
        cuttings_potted += newly_potted
        new_rootstocks += newly_potted
        rootstock.update_acell('d1', cuttings_potted)
        rootstock.update_acell('e1', cuttings_potted)
        print(f"You have now potted up a total of {cuttings_potted} cuttings out of a total of {cuttings_taken}! That means you now have {new_rootstocks} immature rootstocks for grafting next year.")
    else:
        print("Record new cuttings potted action cancelled.")

def Plan_grafting_campaign():
    rootstocks_available = int(rootstock.acell('e2').value)

    row_values = grafts_year_zero.row_values(1)
    first_empty_index = next((i for i, val in enumerate(row_values) if not val), len(row_values))
    last_column = chr(ord('A') + first_empty_index)
    print(last_column)
    name_range = f"c1:{last_column}1"
    value_range = f"c2:{last_column}2"

    row_numbers = [1, 2]

    ranges = [f'A{row}:{last_column}{row}' for row in row_numbers]

    data = {}

    for range_to_read in ranges:
        values =grafts_year_zero.get(range_to_read)[0]
        keys = grafts_year_zero.get(range_to_read.replace(str(row_numbers[0]), str(row_numbers[1])))[0]
        data.update(dict(zip(keys, values)))

    print(data)

    cultivars = grafts_year_zero.get(name_range) [0]
    planned_numbers = grafts_year_zero.get(value_range) [0]
    count = 0
    print(f"For which cultivar would you like to plan a grafting campaign?\
    \nYou currently have {rootstocks_available} rootstocks available for use in grafting. \n")
    for cultivar in cultivars:
        count += 1
        print(f"{count}. {cultivar}")

    print("For which cultivar would you like to plan your grafting?\n")
    cultivar_value = int(input("Please enter the number of the cultivar for which you want to plan grafting (see the cultivar listed above): \n"))

    

def Hold_back():
    print("Stocks held back")

def Bring_forward():
    print("Stocks brought forward")

def Record_loss():
    print("Loss recorded")

def Record_acquisition():
    print("Acquisition_recorded")

def Help():
    print(help_text)

def Startup_error_msg():
    print("Startup error message called")



"""Tell the user they need to start up the program with an argument to make the program actually do anything."""
if len(sys.argv) == 1:
    Startup_instructions()
else:
    parameter = sys.argv[1]
    if parameter == "new_year":
        Create_year()
    elif parameter == "plan_cuttings":
        Plan_cutting_campaign()
    elif parameter == "take_cuttings":
        Record_cuttings_taken()
    elif parameter == "pot_cuttings":
        Record_potted_cuttings()
    elif parameter == "plan_grafting":
        Plan_grafting_campaign()
    elif parameter == "hold_back":
        Hold_back()
    elif parameter == "bring_forward":
        Bring_forward()
    elif parameter == "record_loss":
        Record_loss()
    elif parameter == "record_gain":
        Record_acquisition()
    elif parameter == "help":
        Help()
    else:
        Startup_error_msg()

