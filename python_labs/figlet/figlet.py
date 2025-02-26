# https://cs50.harvard.edu/python/2022/psets/4/figlet/

import sys
import random
from pyfiglet import Figlet

def main():

    # Initialize figlet
    figlet = Figlet()

    # Pull down a list of fonts
    fonts = figlet.getFonts()

    # If the user doesn't include two additional args (i.e., "-f slant" or "--font slant")
    # then per assignment constraints the program should exit immediately with the error message.
    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")

    # Check to see if the user passed two arguments at the command line
    # (should be in format -f <font> or --f <font>)
    if len(sys.argv) == 3:
        # Handling command line arguments (doesn't need to be super robust for the assignment)
        if sys.argv[1] in ["-f", "--font"]:
            # Is the supplied font fount in the list of fonts?
            # Normalize argument to lowercase
            sys.argv[2] = sys.argv[2].lower()
            if sys.argv[2] in fonts:
                # If so, set the figlet font to that value
                figlet.setFont(font=sys.argv[2])
            else:
                # If the font doesn't exist, print error and close
                sys.exit("Invalid usage")
    # If no font was provided using the expected format, choose a random one
    else:
        # Pick a random font by using random.choice(fonts)
        figlet.setFont(font=random.choice(fonts))
    
    # Prompt for input
    phrase = input("Input: ")

    # Print it using the selected font
    print(figlet.renderText(phrase))

if __name__ == "__main__":
    main()