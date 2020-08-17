from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

def get_image_from_url (url, name):
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urlopen(url).read())
    img_temp.flush()
    return File(img_temp, name=f"{name}.jpg")