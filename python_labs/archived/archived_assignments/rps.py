import random

user_choice = input("Choose: rock, paper, or scissors? ").lower()

print("You chose " + user_choice + "\n")

choices = ["rock", "paper", "scissors"]
dice_roll = random.randint(0,2)

print("\nThe computer chose: " + choices[dice_roll] + "\n")

print("And the result is....\n")

if user_choice == choices[(dice_roll + 1) % 3]:
    print("You win! " + user_choice + " beats " + choices[dice_roll])
elif user_choice == choices[((dice_roll) - 1) % 3]:
    print("You lose!" + choices[dice_roll] + " beats " + user_choice)
else:
    print("LOL tie I guess you both picked " + user_choice)