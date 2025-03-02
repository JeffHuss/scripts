# https://cs50.harvard.edu/python/2022/psets/6/pizza/
from tabulate import tabulate
import csv
import sys

def main():
    # Check for the correct number of arguments
    # Should be 2 - if only one, no arg passed
    # if more than two, too many args passed
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Make sure the filename ends in .py
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Try opening it:
    try:
        with open(sys.argv[1]) as file:
            # Instantiate the reader
            reader = csv.DictReader(file)
            # Print it with tabulate, using the existing keys as headers
            # and the grid format for the output
            print(tabulate(reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()