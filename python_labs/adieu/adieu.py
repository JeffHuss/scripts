# https://cs50.harvard.edu/python/2022/psets/4/adieu/

import inflect

def main():
    # Initialize an empty list (will be used to store names)
    names = []

    # Initialize inflect engine (See: https://pypi.org/project/inflect/)
    p = inflect.engine()

    # Loop until 
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print(f"\nAdeiu, adeiu, to {p.join(names)}")
            break


if __name__ == "__main__":
    main()