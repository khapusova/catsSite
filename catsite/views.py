from django.shortcuts import render
import requests

def home(request):
    url = 'https://api.thecatapi.com/v1/images/search'
    dir = r'C:\Users\diana\PycharmProjects\whichCatAreYou\static'

    def savePictureAPI(url, direction):
        response = requests.get(url)
        print(response.text)
        picture_url = (eval(response.text)[0])["url"]
        id = (eval(response.text)[0])["id"]
        r = requests.get(picture_url, allow_redirects=True)
        extent = picture_url.split(".")[-1]
        open(rf'{direction}\{id}.{extent}', 'wb').write(r.content)
        return rf"{direction}\{id}.{extent}"

    return render(request, "homepage.html",{'picture' : savePictureAPI(url,dir)})