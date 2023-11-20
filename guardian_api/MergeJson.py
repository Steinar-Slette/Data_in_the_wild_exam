import glob
import json

result = []
for j in glob.glob("2023_response_page*.json"):
    with open(j, "rb") as infile:
        result.append(json.load(infile))

with open("merged_2023_responses.json", "w") as outfile:
     json.dump(result, outfile)
