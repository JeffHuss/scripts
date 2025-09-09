# https://cs50.harvard.edu/python/2022/psets/4/emojize/

from emoji import emojize

def main():
    # Get user input
    my_emoji = input("Input: ")

    # Output - included the "alias" bucket to account for defined constraints
    print(f"Output: {emojize(my_emoji, language='alias')}")

if __name__ == "__main__":
    main()