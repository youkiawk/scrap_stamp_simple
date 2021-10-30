import requests
from bs4 import BeautifulSoup
import json
import sys

def imageUrl(link, imagename):
    # get HTML
    res = requests.get(link)
    # get beautifulsoup object
    soup = BeautifulSoup(res.text, 'html.parser')
    # extract lists of stamp
    found = soup.find_all('li', class_='mdCMN09Li FnStickerPreviewItem')
    # extract urls or image
    url_list = [json.loads(found[i]['data-preview'])['staticUrl'] for i in range(len(found))]
    # scrap images
    for i, url in enumerate(url_list):
        image = requests.get(url).content
        dst = "output/" + imagename + "/" + str(i) + ".png"
        with open(dst, "wb") as f:
            print("download to: " + dst)
            f.write(image)

if __name__ == "__main__":
    pass
