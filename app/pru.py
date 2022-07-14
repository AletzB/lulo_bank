import requests
import os
import json

url="http://api.tvmaze.com/schedule/web"
args={"date":f"2020-12-01"}
response = requests.get(url, params=args)
if response.status_code == 200:
    response_json = response.json()
    jsonString = json.dumps(response_json)
    with open(f'{args["date"]}.json', 'w') as f:
        f.write(jsonString)
print(jsonString)
    