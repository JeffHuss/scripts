def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    slash = "/"
    comma = ","

    while True:
        # Get the date
        user_date = input("Date: ").strip()

        # Check for a "/" in the date
        if slash in user_date:
            # Assume date is in mm/dd/yyyy format
            parsed_date = user_date.split("/")
            try:
                # Validate that we get an integer for month, day, and year
                # Also make sure that month is in the range of 1-12 (inclusive)
                # and make sure that day is in the range of 1-31 (inclusive)
                # Extract the month
                parsed_month = int(parsed_date[0])
                if not 1 <= parsed_month <= 12:
                    continue
                
                # Extract the day
                parsed_day = int(parsed_date[1])
                if not 1 <= parsed_day <= 31:
                    continue

                # Extract the year
                parsed_year = int(parsed_date[2])
            except ValueError:
                # print(f"{user_date} is in an invalid format! Try again.")
                continue
            else:
                break

        elif comma in user_date:
            # Assume date is in month day, year format
            # First thing, remove the comma so just spaces separate terms
            user_date = user_date.replace(",", "")
            # Split on the spaces
            parsed_date = user_date.split()
            try:
                # Validate that we get an integer for month, day, and year
                # Also make sure that month is in the range of 1-12 (inclusive)
                # and make sure that day is in the range of 1-31 (inclusive)
                # Extract the month
                if parsed_date[0].title() in months:
                    parsed_month = months.index(parsed_date[0]) + 1
                else:
                    continue
                
                # Extract the day
                parsed_day = int(parsed_date[1])
                if not 1 <= parsed_day <= 31:
                    continue

                # Extract the year
                parsed_year = int(parsed_date[2])
            except ValueError:
                # print(f"{user_date} is in an invalid format! Try again.")
                continue
            else:
                break
        else:
            # print(f"{user_date} is in an invalid format! Try again.")
            continue
    
    # Print the result with proper 0-padded format (yyyy-mm-dd)
    print(f"{parsed_year:04}-{parsed_month:02}-{parsed_day:02}")




if __name__ == "__main__":
    main()