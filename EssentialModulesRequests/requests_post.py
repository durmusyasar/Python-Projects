import requests
my_data = {"name": "Durmuş", "email": "durmusyasar.ceng@gmail.com"}
r = requests.post("http://www.w3schools.com/php/welcome.php", data=my_data)

f = open("myfile.html", "w+")
f.write(r.text)