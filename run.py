# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# Now our scope is set, we'll create  another constant variable named creds.
# To do this, we call the from_service_account_file  method of the Credentials class,  
# and we pass it our creds.json file name.
CREDS = Credentials.from_service_account_file('creds.json')

# Now our scope and creds variables  are ready, we’ll create a new variable, 
# called SCOPED_CREDS. Using the  with_scopes method of the creds object,  
# and pass it our scope variable.
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Next, we create our GSPREAD_CLIENT.  
# Using the gspread authorize method,  and pass it our SCOPED_CREDS.
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# And finally, we can access our  love_sandwiches sheet, 
# using the open() method on our client object  and passing it the name we gave our spreadsheet. 
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")

    # We’ll define a new variable called sales_data  
    # and use the split() method on our data string, to break it up at the commas. 
    # This will remove the commas from the string.

    #In order to insert our data into our spreadsheet, our values need to be in a list.
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises Value Error if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_sales_data()

