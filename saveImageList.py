import requests
from bs4 import BeautifulSoup
import csv
import os
import pathlib

def saveImages(imageUrls, prefix):
    i = 0
    for url in imageUrls:
        
        response = requests.get(url)
        image = response.content
//拡張子をダウンロードしたファイルから抽出・3文字の場合　ex. jpg
        extention = url[-5:]
        file_name = prefix + '_' + str(i) + extention
        i+=1

        dir_path = pathlib.Path('./' + prefix)

        if(dir_path.exists()==False):
            dir_path.mkdir()

        file_path = os.path.join(dir_path, file_name)

        with open(file_path, "wb") as f:
            f.write(image)

def ImagesList(items, name):
    csvlist = []
    for item in items:
        src = item.get("src")
        csvlist.append(src)
    saveImages(csvlist, name)
    print(csvlist)

    
urls = []


for url in urls:
    response = requests.get(url)

    bsObj = BeautifulSoup(response.text,"html.parser")
//URLの35番目から最後から２つ目までがファイル名用のslugだったの抽出
    file_name = url[34:-1]
	
    html = bsObj.find(class_="main")
    items = html.find_all("img")

    ImagesList(items, file_name)
