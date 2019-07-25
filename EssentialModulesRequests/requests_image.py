import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://3.bp.blogspot.com/-jY8-cI7KZI4/XFSljhilPPI/AAAAAAAAFGE/yOrbqw0vVD4yEe_MGW6WYEz_Dv13v950QCHMYCw/s1600/epic-hd-backgrounds-wallpaper-cave.jpg")
print("Status Code", r.status_code)
image = Image.open(BytesIO(r.content))
print(image.size, image.format, image.mode)
path = "./image1." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")