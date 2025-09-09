# https://cs50.harvard.edu/python/2022/psets/4/game/

from random import randint

def main():
    # Get input from user - loop to repeat prompt if ValueError or level <= 0
    while True:
        try:
            # Get the input and catch a ValueError if an int isn't entered
            level = int(input("Level: "))
            # Make sure the level is at least 1, repeat prompt otherwise
            if level < 1:
                continue
            break
        # Continue prompting in case of a ValueError
        except ValueError:
            pass
    
    # Calculate a value based on a range provided by the user
    answer = randint(1,level)

    # Loop while collecting guesses - repeat until the answer is guessed
    while True:
        try:
            # Prompt for a guess
            guess = int(input("Guess: "))
        # It needs to be an integer
        except ValueError:
            pass
        # Invalid / out of range guesses will re-prompt the user for a new guess
        # Otherwise, a hint will be given letting the user know if their guess was
        # too small, too large, or just right (at which point the program exits)
        else:
            if guess < 1 or guess > level:
                continue
            if guess < answer:
                print("Too small!")
                continue
            elif guess > answer:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break
 


if __name__ == "__main__":
    main()