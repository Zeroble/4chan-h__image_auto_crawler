import os
from bs4 import BeautifulSoup
import requests
import urllib
import shutil
import threading
import encodings.idna

curPath = "./"
aftPath = "./4chan-h/"
baseURL = "http://boards.4chan.org/h/"
complteCnt = 0

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

class four_chan_h(threading.Thread):
    def __init__(self,page):
        self.page = page
        threading.Thread.__init__(self)

    def run(self):
        global baseURL
        global complteCnt
        if (self.page >= 2):
            URL = baseURL + str(self.page)
        else:
            URL = baseURL

        req = requests.get(URL)
        html = req.text

        soup = BeautifulSoup(html, "html.parser")
        myUrls = soup.select('div.board > div.thread a.fileThumb')
        print(URL)
        for j in myUrls:
            download_Image(j.get('href'),self.page)
        print("{0} page download complete!\n".format(self.page))
        complteCnt+=1


if not os.path.exists("4chan-h"):
        os.makedirs("4chan-h")


for i in range(1,11):
    Thread = four_chan_h(i)
    Thread.start()