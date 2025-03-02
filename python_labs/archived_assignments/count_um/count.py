# https://cs50.harvard.edu/python/2022/psets/7/um/

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Pattern for matching the word "um" with a variable number of "m"
    # characters. Can catch um, ummmm, umm, etc., but not words like
    # "umbrella" or "summary"
    pattern = r"\bum+\b"
    # matches is assigned a list of all matches for the pattern
    # case is ignored so the pattern can be simple (i.e., not needing [uU][mM])
    matches = re.findall(pattern, s, flags=re.IGNORECASE)
    # Since matches is a list of pattern matches, the length of the list
    # represents the count of occurrences.
    count = len(matches)
    return count


if __name__ == "__main__":
    main()