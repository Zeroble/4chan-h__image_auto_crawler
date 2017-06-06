import os
import requests
import urllib
import shutil
from bs4 import BeautifulSoup

curPath = "./"
aftPath = "./4chan-h/"

def download_Image(ImageUrl, page):
    name = ImageUrl[15:]
    ImageUrl = "http:" + ImageUrl
    check = 0
    while (1):
        try:
            urllib.request.urlretrieve(ImageUrl, name)
            check = 10
            print("image name : {0}\nImageUrl : {1}\npage : {3}/10\n".format(name, ImageUrl, check, page))
        except:
            print("ERROR\ncheck : {0}".format(check))
            check += 1
        finally:
            if (check >= 10):
                break
    try:
        shutil.move(curPath + name, aftPath + name)
    except:
        pass


baseURL = "http://boards.4chan.org/h/"

for i in range(1, 11):
    if (i >= 2):
        URL = baseURL + str(i)
    else:
        URL = baseURL

    req = requests.get(URL)
    html = req.text

    soup = BeautifulSoup(html, "html.parser")
    myUrls = soup.select(
        'div.board > div.thread a.fileThumb'
    )

    if not os.path.exists("4chan-h"):
        os.makedirs("4chan-h")
    print(URL)
    for j in myUrls:
        download_Image(j.get('href'),i)

print("download complete!")