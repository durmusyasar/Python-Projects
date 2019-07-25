import requests 
from bs4 import BeautifulSoup

url =  "https://yellowpages.com.tr/ara?q=Ankara" # Site linkimiz 

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.


print(soup.prettify()) # Daha güzel bir görüntü için prettify() fonksiyonunu kullanıyoruz.

print(soup.find_all("a")) # Bize tüm <a> etiketlerini liste şeklinde dönüyor.

for i in soup.find_all("a"):
    print(i.get("href"))

for i in soup.find_all("a"):
    print(i.text)

 # Bu kullanımın anlamı div etiketlerinden class'ı yp-poi-box-2 yi al anlamına geliyor.
for i in soup.find_all("div",{"class":"yp-poi-box-2"}):
    print(i)