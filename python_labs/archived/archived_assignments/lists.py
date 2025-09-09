shopping_items = []

response = "y"

while response == "y":
    user_input = input("\n Please enter an item for the shopping list: ")
    if user_input not in shopping_items:
        shopping_items.append(user_input)
    elif user_input in shopping_items:
        print("\n Sorry but that item was already added!")
    else:
        print("\nSomething majorly weird happened.")
    print("\nSo far the list is: " + str(shopping_items))
    response = input("\nWould you like to add another item (y/n)? ").lower()

print("\nGoodbye!")