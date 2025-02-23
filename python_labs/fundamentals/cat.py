# for i in range(3):
#     print(f"Meow {i+1}")

# j = 0
# while j < 3:
#     print(f"Woof! {j+1}")
#     j += 1

# for i in ["Harry", "Hermione", "Ron"]:
#     print(f"{i}")

# print(f"Meow\n" * j, end="")

def main():
    meow(get_number())

def meow(n):
    print("Meow\n" * n, end="")

def get_number():
    while True:
        try:
            count = int(input("How many times should the cat meow? "))
            if count > 0:
                break
            print("Please make sure to enter a positive number!")
        except ValueError:
            print("You must enter an integer.")
    return count

if __name__ == "__main__":
    main()