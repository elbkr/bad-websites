import json
import glob

result = []
for f in glob.glob("*.json"):
    with open(f, "rb") as infile:
        result.append(json.load(infile))

with open("websites.json", "wb") as outfile:
     json.dump(result, outfile, indent=4)
