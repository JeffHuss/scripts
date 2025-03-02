# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import re
import sys

def main():
    # Prompt for an IP
    ip_address = input("IPv4 Address: ")
    # Print the boolean response from validate() which checks for a valid IP
    # returns True if valid, False otherwise
    print(validate(ip_address))


def validate(ip):
    # Pattern for matching octets in IPv4 address, put into match groups
    ip_pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    # If there's a match, save the match object to `matches` and proceed
    # else, it isn't a valid pattern so return False and don't continue
    # evaluating.
    if matches := re.search(ip_pattern, ip):
        # Try/Except block to catch ValueErrors when converting with int()
        try:
            # Each capture group is an octet in an IPv4 address
            for octet in matches.groups():
                # Octets are only valid in the range of 0-255
                # Since negative numbers won't match the pattern,
                # no need to check for them here.
                if int(octet) > 255:
                    return False
        except ValueError:
            return False
        # All criteria have been checked so return True
        return True
    else:
        return False


if __name__ == "__main__":
    main()