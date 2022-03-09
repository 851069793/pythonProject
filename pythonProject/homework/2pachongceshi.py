import requests
req = requests.get("https://news.sina.com.cn")
req.encoding=(req.text)
print(req.text)
