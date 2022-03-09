# import urllib
#
#
# from urllib import response
# from urllib import request
# import os
#
# url1 = "https://movie.douban.com/top250?start="
# head1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",}
#
# request1 = urllib.request.Request(url=url1,headers=head1)
# resp1 = urllib.request.urlopen(request1).read()
# f=open("豆瓣1.html","wb")
# f.write(resp1)
# f.close()


# baseurl="https://movie.douban.com/top250?start="
# for x in range(0,250,25):
#     s="".join([baseurl,"{}".format(x)])
#     print(s)
# import re
#
# s = '\n                            导演: 卡比尔·汗 Kabir Khan\xa0\xa0\xa0主演: 萨尔曼·汗 Salman Khan / 哈莎莉·马...<br/>\n                            2015\xa0/\xa0印度\xa0/\xa0剧情 喜剧 动作\n                        '
# s= re.sub(r"(\s+)","",s)
# s= re.sub(r"<br/>","",s)
#
# print(s)

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, xlwt.Formula('HYPERLINK("http://www.google.com";"Google")')) # Outputs the text "Google" linking to http://www.google.com
workbook.save('Excel_Workbook.xls')

