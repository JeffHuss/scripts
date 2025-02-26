def main():
    # Initialize the empty dict
    list = {}

    # Start a loop for user input that will terminate when
    # it catches Ctrl+D (EOFError exception)
    while True:
        try:
            # Get an item from the user and convert to UPPERCASE
            item = input().upper()
            # Default value is 0 - add 1 each time the item is input
            list[item] = list.get(item,0) + 1
        except EOFError:
            # When user inputs Ctrl+D exit the loop and we'll move on
            # to where the list is sorted and printed
            break

    # Dictionaries can't be sorted in place so extract key:values as tuples,
    # sort them by key, convert the list of tuples back to a dictionary,
    # and then assign the resulting dictionary back to the list variable.
    # list is now an alphabetially-sorted dictionary
    list = dict(sorted(list.items()))

    # Iterate over each item in the list and print out the value (aka count)
    # followed by the item name
    for item in list:
        print(f"{list[item]} {item}")


if __name__ == "__main__":
    main()