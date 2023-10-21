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

cutting_success = rootstocks_potted / cuttings_taken
potting_success = mature_rootstocks / rootstocks_potted

rootstock_data = rootstock.get_all_values()
print(rootstock_data)

def Startup_instructions():
    print(startup_instructions)

def Create_year():
    rootstock_year = rootstock.acell('a1').value
    new_rootstock_year = int(rootstock_year) + 1

    print(f"The last year created was {rootstock_year}")
    cuttings_last_year = rootstock.acell('c2').value
    if input(f"Would you like to create a record for {new_rootstock_year}? Type 'y' for yes and 'n' for no: ").lower() == 'y':
        print(f"\nInfo: You took {cuttings_taken} cuttings last year and successfully potted {rootstocks_potted} ({round(cutting_success * 100)}%) of them.\
        \nYou currently have {mature_rootstocks} maturing rootstocks in stock.\n")
        num_cuttings = int(input(f"How many cuttings would you like to plan for {new_rootstock_year}? \
        \n(Enter 0 if you would like to plan the number of cuttings to be taken later): "))
        values = [new_rootstock_year, num_cuttings, 0, 0, 0]
        rootstock.insert_row(values)  
        print(f"Year {new_rootstock_year} created. {num_cuttings} cuttings planned for this year.")
        if num_cuttings == 0:
            print("You've chosen to plan your cutting campaign later!")

        graft_starting_values = [
            [2023, 'planned', 0, 0, 0, 0, 0, 0],
            [2023, 'grafted', 0, 0, 0, 0, 0, 0],
            [2023, 'stock', 0, 0, 0, 0, 0, 0],
            ]

        grafts_year_zero.insert_rows(graft_starting_values, 2)


    else:
        print(f"The year {new_rootstock_year} has not been created. The current year is still {rootstock_year}")

def Plan_cutting_campaign():
    print("Cuttings campaign planning completed")

def Record_cuttings():
    print("Cuttings completed")

def Record_potted_cuttings():
    print("cuttings potted")

def Plan_grafting_campaign():
    print("Grafting campaign planning completed")

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

if len(sys.argv) == 1:
    Startup_instructions()
else:
    parameter = sys.argv[1]
    if parameter == "new_year":
        Create_year()
    elif parameter == "plan_cuttings":
        Plan_cutting_campaign()
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

