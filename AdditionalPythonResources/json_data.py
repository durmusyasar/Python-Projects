import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json")
    data = json.loads(old_file.read())
    print("Current age is ", data["age"], "---addinga year")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name" : "Durmus", "age" : 25}
    print("No file found setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))