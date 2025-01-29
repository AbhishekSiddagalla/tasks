import re
from datetime import datetime
def parsing_date(file_name):
    try:
        search_date = re.findall(r"(0[1-9]|1[0-2])"  #month
                                 r"(0[1-9]|[12][0-9]|3[01])"  #date
                                 r"(20[0-9]{2})",    #year
                                 file_name)
        if not search_date:
            return "Date Not Found"
        # print(search_date)
        search_date = "".join(search_date[0])
        # print(search_date)
        processed_date = datetime.strptime(search_date,"%m%d%Y")
        formatted_date = processed_date.strftime("%b-%d-%Y") # Converting Extracted date in the format of MM-DD-YYYY
        return formatted_date
    except (IndexError,ValueError) as e:
        return "Invalid Date"

file_name = "NAV Portfolio Notebook_ELEQUIN INVESTMENTS, LLC_11052024.XLSX" #contains single date
# file_name2 = "NAV Portfolio Notebook_ELEQUIN INVESTMENTS, LLC_02232001.XLSX" #contains multiple dates
# file_name3 = "NAV Portfolio Notebook_ELEQUIN INVESTMENTS, LLC_24542024.XLSX" #contains invalid date format
print(parsing_date(file_name)) # function call1
# parsing_date(file_name2) # function call2
# parsing_date(file_name3) # function call3