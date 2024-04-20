from datetime import date, timedelta, datetime
import re

def validate_date(date_str):
    """
    This function validates if the input string is in the format "DD-MM-YYYY".
    """
    try:
        # Define the regex pattern for date format "DD-MM-YYYY"
        date_pattern = r'^\d{2}-\d{2}-\d{4}$'
        # Check if the date string matches the pattern
        if re.match(date_pattern, date_str):
            return True
        else:
            return False
        return True
    except ValueError:
        return False


def get_weeks_between(startDate_str, endDate_str):
    """
    This function calculates the weeks between two dates, considering only full weeks 
        (from Monday till Sunday must be in the period between startdata and enddate)
    and list Mondays as output.

    @input:
        date1_str: The first date string in the format "DD-MM-YYYY".
        date2_str: The second date string in the format "DD-MM-YYYY".

    Returns:
        A list of Mondays (datetime objects) between the two dates, considering only full weeks.
    """

    if not validate_date(startDate_str) or not validate_date(endDate_str):
        raise ValueError("Invalid date format. Please use DD-MM-YYYY.")

    date_format = '%d-%m-%Y'

    startDate = datetime.strptime(startDate_str, date_format)
    date2 = datetime.strptime(endDate_str, date_format)
    
    # Swap dates if necessary to ensure date1 is before date2
    if startDate > date2:
        startDate, date2 = date2, startDate
        
    auxDate = startDate

    # Move date1 to the previous Monday (if not already Monday)
    while auxDate.weekday() != 0:
        auxDate -= timedelta(days=1)

    weeks = []
    while auxDate <= date2:
        if (auxDate >= startDate and auxDate <= date2 and (auxDate + timedelta(days=7)  <= date2)):
            weeks.append(auxDate)
        auxDate += timedelta(days=7)

    return weeks


# Example usage
date1_str = "01-11-2024"
date2_str = "30-11-2024"

date3_str = "01-01-2024"
date4_str = "31-12-2024"

date5_str = "30-04-2024"
date6_str = "01-04-2024"

date7_str = "30/04/2024"
date8_str = "01-04-2024"

try:
    print('Test for ', date1_str, ' and ', date2_str)
    mondays1 = get_weeks_between(date1_str, date2_str)
    for monday in mondays1:
        print(monday.strftime("%d-%m-%Y"))
   
    print('Test for ', date3_str, ' and ', date4_str)
    mondays2 = get_weeks_between(date3_str, date4_str)
    for monday in mondays2:
        print(monday.strftime("%d-%m-%Y"))

    print('Test for ', date5_str, ' and ', date5_str)
    mondays3 = get_weeks_between(date5_str, date6_str)
    for monday in mondays3:
        print(monday.strftime("%d-%m-%Y"))
        
    print('Test for ', date7_str, ' and ', date8_str, 'here will be an error in date format')
    mondays4 = get_weeks_between(date7_str, date8_str)
    for monday in mondays4:
        print(monday.strftime("%d-%m-%Y"))
    
except ValueError as e:
    print(e)