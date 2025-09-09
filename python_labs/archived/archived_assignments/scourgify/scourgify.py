# https://cs50.harvard.edu/python/2022/psets/6/scourgify/
import sys
import csv


def main():
    # Check for the correct number of arguments
    # Should be 3 - first is file input and second
    # is file output. Both should have .csv suffix
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Make sure the filenames end in .csv
    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not valid CSV files")

    # Try opening the input file:
    try:
        with open(sys.argv[1]) as file_in, open(sys.argv[2], "w") as file_out:
            # Initialize reader object
            reader = csv.DictReader(file_in)
            # Initialize writer object with new filenames and the adjusted column headers
            writer = csv.DictWriter(file_out, fieldnames=["firstname","lastname","house"])
            # Write the headers
            writer.writeheader()
            # Iterate over the rows in the reader
            for row in reader:
                # Extract fullname as a list where [0] = last and [1] = first
                fullname = row["name"].split(",")
                # Write rows with the desired K:Vs making sure to strip()
                # leading/trailing whitespace
                writer.writerow(
                    {
                        "firstname": fullname[1].strip(),
                        "lastname": fullname[0].strip(),
                        "house": row["house"]
                    }
                )
    except FileNotFoundError:
        sys.exit("Input file does not exist")



if __name__ == "__main__":
    main()