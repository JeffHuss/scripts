# https://cs50.harvard.edu/python/2022/psets/7/working/

import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    # Define a pattern that matches all acceptable time formats:
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM
    # 9:00 AM to 5 PM
    # 9 AM to 5:00 PM
    # Expect that AM and PM will be capitalized (with no periods therein)
    # and that there will be a space before each. Assume that these times
    # are representative of actual times, not necessarily
    # 9:00 AM and 5:00 PM specifically.
    
    pattern = r"^(?P<first_hours>\d?\d)(?::|\s)?(?P<first_minutes>\d\d)?\s?(?P<first_ampm>(AM|PM))\sto\s(?P<second_hours>\d?\d)(?::|\s)?(?P<second_minutes>\d\d)?\s?(?P<second_ampm>(AM|PM))$"

    if matches := re.search(pattern, s):

        # Try to convert first_hours to an int
        # Raise a ValueError if this fails
        try:
            first_hours = int(matches.group("first_hours"))
            if first_hours > 12:
                raise ValueError
        except ValueError:
            raise ValueError("Invalid 'hours' for first clock time.")
        
        # Check if there was a match for the first_minutes capture group
        # If there was, try to convert it to an int and raise a ValueError
        # exception if that fails.
        if matches.group("first_minutes"):
            try:
                first_minutes = int(matches.group("first_minutes"))
                if first_minutes >= 60:
                    raise ValueError
            except ValueError:
                raise ValueError("Invalid 'minutes' for first clock time.")
        # If that capture group did not match, set minutes to 0
        else:
            first_minutes = 0

        # Determine for the first time whether AM (firstampm = 0)
        # or PM (first_ampm = 1). This will be used to convert the
        # hours to 24-hour format in a later step
        try:
            if matches.group("first_ampm") == "AM":
                first_ampm = 0
            elif matches.group("first_ampm") == "PM":
                first_ampm = 1
            else:
                raise ValueError
        except ValueError:
            raise ValueError(f"Invalid 'first_ampm' - expected either AM or PM but found {matches.group("first_ampm")}")
        
        # Try to convert second_hours to an int
        # Raise a ValueError if this fails
        try:
            second_hours = int(matches.group("second_hours"))
            if second_hours > 12:
                raise ValueError
        except ValueError:
            raise ValueError("Invalid 'hours' for second clock time.")
        
        # Check if there was a match for the second_minutes capture group
        # If there was, try to convert it to an int and raise a ValueError
        # exception if that fails.
        if matches.group("second_minutes"):
            try:
                second_minutes = int(matches.group("second_minutes"))
                if second_minutes >= 60:
                    raise ValueError
            except ValueError:
                raise ValueError("Invalid 'minutes' for second clock time.")
        # If that capture group did not match, set minutes to 0
        else:
            second_minutes = 0
        
        # Determine for the second time whether AM (second_ampm = 0)
        # or PM (second_ampm = 1). This will be used to convert the
        # hours to 24-hour format in a later step
        try:
            if matches.group("second_ampm") == "AM":
                second_ampm = 0
            elif matches.group("second_ampm") == "PM":
                second_ampm = 1
            else:
                raise ValueError
        except ValueError:
            raise ValueError(f"Invalid 'second_ampm' - expected either AM or PM but found {matches.group("second_ampm")}")
        
        # Convert the hours to 24-hour format
        # first_ampm/second_ampm are 0 for AM and 1 for PM
        # this will properly set the base clock, which I will
        # add to first_hours/second_hours % 12, which leaves the appropriate remained
        # E.g.
        # 9 AM = (12 * 0) + 9 = 9
        # 12 PM = (12 * 1) + 0 = 12
        # 5 PM = (12 * 1) + 5 = 17
        first_hours = (12 * first_ampm) + (first_hours % 12)
        second_hours = (12 * second_ampm) + (second_hours % 12)

        return f"{first_hours:02}:{first_minutes:02} to {second_hours:02}:{second_minutes:02}"
  
    else:
        raise ValueError  


if __name__ == "__main__":
    main()