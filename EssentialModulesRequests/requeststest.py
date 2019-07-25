import requests

params = {"#q": "pizza"}
r = requests.get("http://google.com", params=params)
print("Status : ", r.status_code)

print(r.url)

f = open("./page.html", "w+")
f.write(r.text)