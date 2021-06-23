from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import easyocr
import string
import random

def index(request):
    flag = 0
    # getting image and storing into media folder -
    if request.method == 'POST':
        flag = 1
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        file_location = fs.url(filename)
        print(file_location, " ************")
        # Fetching text out of image -
        reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
        print("1st ---")
        if settings.DEBUG:
            result = reader.readtext('E:/OCR/{}'.format(file_location))
        else:
            result = reader.readtext('{}'.format(file_location))
        print("2nd ---")
        s  = ""
        for i in result:
            s = s + i[1] + " "
            print(i[1])
        return render(request, "main/index.html", {'s': s, 'flag':flag})
    return render(request, "main/index.html", {'flag':flag})
