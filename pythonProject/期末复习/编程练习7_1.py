import json
import requests

import bs4

baseurl = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
req = requests.get(url=baseurl,headers=header)
a = req.content.decode()
movie = json.loads(a)
for m in movie["subjects"]:
    print("{}:{}".format(m["title"],m["rate"]))