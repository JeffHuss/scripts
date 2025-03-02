# https://cs50.harvard.edu/python/2022/psets/7/response/

from validator_collection import validators
import validator_collection.errors

"""
In a file called response.py, using either validator-collection or validators from PyPI,
implement a program that prompts the user for an email address via input and then prints
Valid or Invalid, respectively, if the input is a syntatically valid email address.
You may not use re. And do not validate whether the email address’s domain name actually exists.
"""

def main():
    print(validate(input("What's your email? ")))


def validate(email):
    try:
        validators.email(email)
        return "Valid"
    except validator_collection.errors.InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()