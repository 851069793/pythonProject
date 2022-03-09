import jieba
import wordcloud
from imageio import imread
f=open('51job.csv', 'r', encoding='utf-8')
txt1=f.readlines()
txt=''
for i in txt1:
     print('----------')
     print ('line from txt1: ',i)
     txt=txt+i
     print("joined........",txt)
     print('.........')
print(txt)
mk=imread("wujiaoxing.png")
w = wordcloud.WordCloud( font_path="msyh.ttc",mask=mk,background_color = "white")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("csv_cloud1.png")