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

# Now we have our sheet variable defined, let’s  try to access the data in our sales worksheet.
sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)