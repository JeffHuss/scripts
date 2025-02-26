import requests
import sys
import json

def main():
    # Ask the user for a search term
    search_term = input("Search term: ")

    # Ask the user for a limit to the number of results
    # Catch error for non-INT value and retry
    while True:
        try:
            limit = int(input("How many results would you like? "))
        except ValueError:
            print(f"{limit} is not a valid integer.")
        else:
            break
    
    # Pass the search term and limit to get_artworks which will query the API
    # with those parameters and return the results (values for the "data" key)
    artworks = get_artworks(search_term,limit)
    
    # Each object under key "data" in the response represents a result for the query
    # Loop through them and print out the title of each object
    for art in artworks:
        print(f"* {art['title']}")


def get_artworks(q, l):
    
    # Endpoint from the API documentation on their website
    url = "https://api.artic.edu/api/v1/artworks/search"

    # Try block to catch HTTP status codes that indicate a client or host failure
    # If it fails, exit the program
    try:
        r = requests.get(url, params={"q": q, "limit": l})
        r.raise_for_status()
    except requests.HTTPError as e:
        print("Request failed:", e)
        sys.exit()
    return r.json()["data"]


if __name__ == "__main__":
    main()