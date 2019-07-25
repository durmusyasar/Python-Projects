import requests
import simplejson as json
url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "https://example.com"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers) 

print(r.text)
# print(json.loads(r.text)["error"]["code"])