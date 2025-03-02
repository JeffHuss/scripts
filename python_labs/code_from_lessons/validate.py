# https://cs50.harvard.edu/python/2022/weeks/7/

import re

email = input("What's your email? ").strip().lower()

if re.search(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
    print("Valid")
else:
    print("Invalid")