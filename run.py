import gspread
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
stocks = SHEET.worksheet('stock')


data = stocks.get_all_values()
print(data)

def Startup_instructions():
    print("You must enter an argument after the program script name to use this program. Entering 'run.py' on the command line is not enough. you must enter 'run.py nnnn' (where nnnn is one of the functions that the program contains). For a full list of the program's functions and how to call them, enter 'run.py help' on the command line. Always be careful to use only lower case letters")

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
    print("Help called")

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

