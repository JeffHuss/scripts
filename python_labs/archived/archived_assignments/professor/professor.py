# https://cs50.harvard.edu/python/2022/psets/4/professor/

from random import randint

def main():

    # Ask the user to input a level
    level = get_level()

    # Initialize score to 0 points
    score = 0
    # response = 0

    # No need to reference the iterator because the program
    # will always ask 10 questions
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        for tries in range(3):
            try:
                response = int(input(f"{x} + {y} = "))
                if answer != response:
                    raise ValueError
            except ValueError:
                if tries < 2:
                    print("EEE")
                    continue
                else:
                    print(f"{x} + {y} = {answer}")
                    break
                # print(f"Score: {score} out of {j + 1} possible points.")
            if response == answer:
                score += 1
                # print(f"Score: {score} out of {j + 1} possible points.")
                break
            
    
    print(f"Score: {score}")
    

# Get a level from the user - (can be 1, 2 or 3)
# The level is subsequently used by generate_integer()
# to determine how many digits the numbers should be
# i.e. 1 = 1 digit numbers, 2 = 2 digit numbers, etc.
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level            
        except ValueError:
            pass

# Takes an integer parameter "level" and generates
# a random integer with that number of digits
def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    elif level == 3:
        return randint(100,999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()