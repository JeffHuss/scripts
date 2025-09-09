# https://cs50.harvard.edu/python/2022/weeks/7/

import re

def main():
    url = input("URL: ").strip()
    
    if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)/?.*$", url, re.IGNORECASE):
        print(f"Username:", matches.group(1))

if __name__ == "__main__":
    main()