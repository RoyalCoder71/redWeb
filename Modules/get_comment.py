# NOT DEVELOPED YET

import requests

url = "https://www.virustotal.com/api/v3/domains/google.com/comments?limit=20"

api_key = "{Your API Key}"

headers = {'x-apikey':api_key,"accept": "application/json"}

response = requests.get(url, headers=headers)
json_response = response.json()

data = json_response["data"]

for datum in data:
    text = datum["attributes"]["text"]
    print(text)

# print(json_response.text)
