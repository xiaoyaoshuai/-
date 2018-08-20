---
title: 爬取图片
tags: 
notebook: 爬虫
---
#爬取尤果网模特图片并保存
```
from bs4 import BeautifulSoup
import requests,shutil
for i in range(11,42):
    c = requests.get('https://www.ugirls.com/Content/Page-{}.html'.format(i))
    c_soup =  BeautifulSoup(c.text)
    for i in c_soup.findAll("a", {"class": "magazine_item_wrap"}):
        girl_url = i['href']
        cont_page = requests.get(girl_url)
        cont_soup = BeautifulSoup(cont_page.text)
        div = cont_soup.findAll("div", {"class": "yang auto"})
        img = div[0].findAll('img')
        for i in img[0:3]:
            name=i['alt']
            url = i ['src']
            response = requests.get(url, stream=True)
            with open('/home/ws/PycharmProjects/untitled/作业/code/picture/{}.jpg'.format(name), 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
```

