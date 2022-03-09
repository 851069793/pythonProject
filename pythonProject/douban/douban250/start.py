import re
from time import sleep

import bs4
from bs4 import BeautifulSoup
import xlwt
import urllib
from urllib import request

baseurl = "https://movie.douban.com/top250?start="  # 豆瓣250的起始网址
datelist = []  # 存放所有电影信息
savepath = "豆瓣电影Top250.xls"


# 1爬取网页
def askurl(url1):
    """
    模仿浏览器打开一个网页
    :param url:
    :return:
    """
    header1 = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664.110Safari / 537.36",
        "Cookie": "bid=NF1jaA5LNAQ; ap_v=0,6.0"}
    request1 = urllib.request.Request(url=url1, headers=header1)
    html1 = urllib.request.urlopen(request1).read().decode("utf-8")  # 编码格式utf-8

    return html1


#     print(html1)
# askurl(0)

def allurl():
    """
    循环解析所有网页
    :return:
    """

    for x in range(0, 250, 25):
        url1 = "".join([baseurl, "{}".format(x)])
        html1 = askurl(url1)
        soup = bs4.BeautifulSoup(html1, "html.parser")

        for item in soup.find_all("div", class_='item'):
            date = []  # 存放一部电影的所有信息
            # print(type(item))
            item = str(item)   #item类型为#<class 'bs4.element.Tag'>
            name = re.findall(r'<span class="title">(.*?)</span>',item)[0]
            # print(name)
            no =  re.findall(r'<em class="">(.*?)</em>',item)[0]
            graphlink = re.findall(re.compile(r'<img.*src="(.*?)"',re.S),item)[0]
            href = re.findall(r'<a href="(.*?)">',item)[0]
            actor1 = re.findall(re.compile(r'<div class="bd">.*?<p class="">(.*?)</p>',re.S),item)[0]    #可能存在问题
            actor2 = re.sub(r"(\s+)","",actor1)
            actor3 = re.sub(r"<br/>","",actor2)
            grade = re.findall(r'<span class="rating_num" property="v:average">(.*?)</span>',item)[0]
            judgenum = re.findall(r'<span>(\d*?)人评价</span>',item)[0]
            date=[no,name,grade,href,graphlink,actor3,judgenum]
            datelist.append(date)
            # print(date)
    print("电影所有数据已存入datelist中")
    return datelist

# 3保存数据
def datesave(datelist,savepath):
    print("开始存入Excel中")
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet(sheetname="豆瓣评分前250")
    sheet.col(3).width= 10000  #设置单元格列宽   自定义
    sheet.col(4).width = 8888*2
    sheet.col(5).width = 8888
    col = ["排名","电影名","评分","电影链接","电影剧照链接","电影信息","评价人数"]
    for x in range(0,len(col)):
        sheet.write(0,x,col[x])         #将列名输入
    for num in range(0,len(datelist)):
        date = datelist[num]
        print("输入第%d条数据中" %(num+1))
        for num2 in range(0,len(date)):
            sheet.write(num+1,num2,date[num2])

    book.save(savepath)
    print("保存成功")


def main():
    datelist=allurl()
    datesave(datelist,savepath)

if __name__== "__main__":
    main()
    print("执行成功")
    temps = input("\n")





