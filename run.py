import gspread
from google.oauth2.service_account import Credentials
import sys

startup_instructions = "You must enter an argument after the program script name to use this program.\
    \nSimply entering 'run.py' on the command line is not enough.\
    \nYou must enter a command in the form 'run.py nnnn' (where 'nnnn' is the name of one of the functions that the program contains).\
    \nFor a full list of the program's functions and instructions on how to call them, enter 'run.py help' on the command line.\
    \nAlways be careful to use only lower case letters."

help_text = "\nc#############################################################################################################################################################\
    \n\nTo run this program you need to call the script file containing its code ('run.py') followed by a space and the name of the operation you want to execute.\
    \nPlease enter one of the operations available using exactly the spelling shown below, and remembering that the names are case sensitive.\
    \nFor example, if you want to plan your cutting production for the year, carefully type 'run.py plan_cuttings' on the command line.\
    \n\nThe following is a list of the operations that this program can help you execute:\
    \n\n    help:          Produces this information message. It shows you how to use this program.\
    \n\n    plan_cuttings: This operation asks you to enter the number of cuttings you wish to produced of your currently preferred rootstock.\
    \n\n    plan_grafting: This operation first asks you to choose the cultivar for which you wish to produce grafts.\
    \n                   It then asks you to enter the number of grafts you wish to produce, giving you the information on how many root stocks are currently available.\
    \n\n    record_loss:   This operation asks you to choose the cultivar and age of the plants for which you want to record a loss.\
    \n                   It then asks you how many plants of that cultivar and age you have lost.\
    \n\n    record_gain:   This operation asks you to choose the cultivar and age of the plants for which you want to record an acquisition or other gain.\
    \n                   It then asks you how many plants of that cultivar and age you have gained or acquired.\
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
stocks = SHEET.worksheet('stock')


data = stocks.get_all_values()
print(data)

def Startup_instructions():
    print(startup_instructions)

def Create_year():
    print("Year created")

def Plan_cutting_campaign():
    print("Cuttings campaign completed")

def Plan_grafting_campaign():
    print("Grafting campaign completed")

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

