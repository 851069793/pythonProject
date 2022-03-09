import urllib.request

url = r"https://www.runoob.com/python3/python-uwsgi.html"
request1 = urllib.request.Request(url,headers={})
resp = urllib.request.urlopen(request1).read()
print(resp)