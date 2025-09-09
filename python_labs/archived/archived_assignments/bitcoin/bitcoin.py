# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import sys

def main():
    # Test for the presence of a command-line argument
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # Test to make sure that the command-line argument can be converted to float
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Make sure user is asking for a positive integer (-1 bitcoins makes no sense, for example)
    if num_bitcoins <= 0:
        sys.exit("Invalid number of bitcoins")

    # Try requesting bitcoin details from https://api.coincap.io/v2/assets/bitcoin
    try:
        r = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        r.raise_for_status()
    except requests.HTTPError:
        sys.exit("There was an error retrieving the data")
    except requests.RequestException:
        sys.exit("There was an error retrieving the data")

    # Put the response JSON into a variable as a dictionary
    o = r.json()
    
    # First make sure that it can be converted to a float, otherwise exit with an error
    try:
        price = float(o["data"]["priceUsd"])
    except ValueError:
        sys.exit("There was an error with the format of the price returned by the API")

    # Print the price multiplied by the user's input, with comma separators truncated to 4 decimal places
    print(f"${price * num_bitcoins:,.4f}")


if __name__ == "__main__":
    main()