# https://cs50.harvard.edu/python/2022/psets/6/lines/
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
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    # Try opening it:
    try:
        with open(sys.argv[1]) as file:
            print(count_rows(file))
    except FileNotFoundError:
        sys.exit("File does not exist")

# Count the number of rows that aren't empty (only whitespace)
# and aren't comments (start with #)
# Returns the count of remaining lines
def count_rows(f):
    count = 0
    for line in f:
        if line.startswith("#"):
            continue
        if len(line.strip()) == 0:
            continue
        count += 1
    return count

if __name__ == "__main__":
    main()
