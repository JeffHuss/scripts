import requests
import json
import sys

def main():
    url = "https://api.artic.edu/api/v1/artworks/search"

    search_term = input("This script submits a query to the API for the Art Institute of Chicacgo!\nPlease enter a search term: ")

    try:
        r = requests.get(url, {"q": search_term})
        r.raise_for_status()
    except requests.HTTPError:
        print("I couldn't complete the request!")
        sys.exit()
    o = r.json()
    for artwork in o["data"]:
        print(f"* {artwork["title"]}")

    # Print the response
    # print(r)

    # Print the JSON blob
    # print(o)

    # print(json.dumps(o, indent=2))


if __name__ == "__main__":
    main()