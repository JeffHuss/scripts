def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Initially the total cost is 0 because no items have been selected
    total = 0

    # Continue asking for input until a ctrl+D (EOFError) is caught
    while True:
        try:
            # Get the item and convert to title case, to match the menu
            item = input("Item: ").title()
            # If the item is in the menu, add the cost to total
            try:
                total += menu.get(item)
            # Catch key error
            except TypeError:
                # print(f"Type Error happened! Oops! {item} not found in menu!")
                continue
            # Print the running total
            print(f"Total: ${total:.2f}")

        # If the user enters Ctrl+D stop execution    
        except EOFError:
            print()
            break

if __name__ == "__main__":
    main()