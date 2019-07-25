from PIL import Image,ImageFilter

image = Image.open("kus.jpg") # aç

image.save("kus2.jpg") # farklı kaydet

image.rotate(180).save("kus3.jpg") # döndür kaydet


image.rotate(90).save("kus4.jpg")

image.convert(mode = "L").save("kus5.jpg") # siyah beyaz yap

degistir = (960,600) 

image.thumbnail(degistir) # ebat degistirme

image.save("kus6.jpg")

image.filter(ImageFilter.GaussianBlur(10)).save("kus8.jpg") # Blurlama

kırpılacak_alan = (340,0,950,600)

image2 = Image.open("ataturk.jpg")
image2.crop(kırpılacak_alan).save("ataturk2.jpg")



# image.show()

