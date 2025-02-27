def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(t):
    if not valid_length(t):
        # print(f"valid_length() was called and returned False")
        return False
    return check_character_ordering(t)

def check_character_ordering(u):
    # print(f"Calling check_character_ordering({u})")
    # Counter to track number of consecutive letters from beginning
    # Returns True if it starts with 2+ letters, otherwise False - DONE
    x = 0
    for i in range(len(u)):
        if u[i].isalpha():
            x += 1
        else:
            break
    # Returns True if the string begins with 2 letters else False
    # print(f"check_character_ordering() was called. Starts with at least 2 letters? {x >= 2}")
    return x >= 2 and check_digit_ordering(u, x)

def valid_length(u):
    # Returns True if the string is between 2 and 6 characters long else False - DONE
    # print(f"valid_length() was called. Contains between 2 and 6 characters? {len(u) >= 2 and len(u) <= 6}")
    return len(u) >= 2 and len(u) <= 6

def check_digit_ordering(u, x):
    # print(f"check_digit_ordering({u} was called and will start checking at index {x}.")
    if x < len(u):
        if u[x] == "0":
            # print(f"The number segment beginning at index {x} starts with a 0, which is invalid.")
            return False
        for i in range(x, len(u)):
            if not u[i].isdigit():
                # print(f"A digit was followed by a non-digit.")
                return False
    # print(f"{u} does indeed end with numbers, and the sequence of numbers does not begin with 0")
    return True

main()