import json
import requests
import sys

if (len(sys.argv) != 2):
    print("Usage: python itunes.py <search term>")
    sys.exit(1)


response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
o = response.json()
for result in o["results"]:
    print(result["trackName"] + " by " + result["artistName"])