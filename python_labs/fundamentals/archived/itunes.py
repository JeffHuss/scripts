import requests
import sys
import json

def main():
    if len(sys.argv) != 2:
        sys.exit()

    r = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
    print(json.dumps(r.json(), indent=2))

    o = r.json()

    for result in o["results"]:
        print(result["trackName"])


if __name__ == "__main__":
    main()