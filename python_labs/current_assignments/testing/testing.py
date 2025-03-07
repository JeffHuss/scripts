# Playing around
import requests
import json
import sys

def main():
    # Define a URL (just using a static URL for now)
    url = "https://rickandmortyapi.com/api/character"

    # Try querying the endpoint for a response
    try:
        r = requests.get(url)
        r.raise_for_status()
    # If the response doesn't have an HTTP status code of 200, print an error and exit
    except requests.HTTPError:
        print("Request could not be completed. Was the API endpoint valid?")
        sys.exit()

    # Put the JSON portion of the response body into blob
    blob = r.json()

    # Get the total number of pages
    count_pages = blob['info']['pages']

    # Start with an empty list that will be filled with dictionary results
    combined_data = []

    # Loop over all the pages
    for i in range(1, count_pages + 1):
        # Print this so the user can follow progress
        print(f"Fetching page {i} of {count_pages}")
        # Request page={i}
        r = requests.get(url,params={'page': i})
        # Extract the JSON blob
        page_data = r.json()
        # Extend 
        combined_data.extend(page_data['results'])

    characters = []

    for result in combined_data:
        characters.append({'id': result['id'], 'name': result['name']})

    print(json.dumps(sorted(characters, key=lambda x: x['id']), indent=2))


if __name__ == "__main__":
    main()