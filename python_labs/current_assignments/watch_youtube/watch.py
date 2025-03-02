# https://cs50.harvard.edu/python/2022/psets/7/watch/

import re
import sys

def main():
    # Prompt the user for an HTML block that may contain
    # an embedded YouTube link
    url = input("HTML: ")
    # Print the returned value after passing the user-provided
    # URL to the parse() function
    print(parse(url))



# Parse a url argument and return the shortened URL
# i.e. http://youtube.com/embed/xvFZjo5PgG0 becomes
# http://youtu.be/xvFZjo5PgG0
def parse(url):

    # Initialize the base URL string
    shortened_url_prefix = "https://youtu.be/"

    # This pattern looks for an opening iframe tag, followed by a src="" property
    # http(s):// and www. are optional. The key can be found after /embed/
    # but can potentially contain query parameters, so I added a check for that.
    pattern = r".*<iframe.*src=\"(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)\??.*\""

    # If there's a match, extract the captured group
    # and return the shortened url prexic concatenated with
    # the captured video ID
    if matches:= re.search(pattern, url, re.IGNORECASE):
        return shortened_url_prefix + matches.group(1)

    # If there is no match, return None
    else:
        return None
    


if __name__ == "__main__":
    main()