# phrase = input("Hey bro what's your name? ")
# print(f"Hello, {phrase}", phrase, sep=":", end="\n\n\n\n")
# print("this is supposed to be a new line")
# print(phrase.encode(encoding="utf-8"))

# my_list = ["First thing", "Second thing", "Third thing"]
# print(' '.join(my_list))
# print(my_list[0].title().strip('Fg'))

# static_number = 1287910.29819
# some_number = float(input("Enter a number: "))
# answer = round(static_number/some_number, 5)
# print(f"{static_number:,} divided by {some_number:,} rounded to the fifth decimal place is: {answer:,}")

# def hello():
#     name = input("What's your name? ").title()
#     print(f"Hello, {name}")

# hello()

# def main():
#     x = int(input("Enter any integer: "))
#     print(f"x squared is {square(x):,}")

# def square(x):
#     return x ** 2

# main()

# def raise_exponent(x,y):
# #    print(f"The function is has been called!")
#     if y == 1:
#         return x
#     return x * raise_exponent(x, y - 1)

# x = int(input("Please enter a number: "))
# y = int(input("Please enter an exponent: "))
# print(f"{x} to the power of {y} is {raise_exponent(x,y)}")

# x = int(input("Enter a number: "))
# if x % 2 == 1:
#     print(f"{x} is odd.")
# else:
#     print(f"{x} is even.")

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")