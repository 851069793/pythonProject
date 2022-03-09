#导入pandas相关的库并查看数据集情况
import os
import re
from collections import Counter

import pandas as pd
import openpyxl
from pyecharts import options as opts
from pyecharts.charts import Line, Pie, Map
from pywin.Demos.ocx import webbrowser

date=pd.read_excel("accesslog.xlsx")
# date.head()
# date.info()
# print(date)
# print('每个独立访客的访问次数'.center(50,"-"))
# pv=round((len(date) / 10000), 3)
# print(f"PV:{pv}万")
# uvlen=len(date.groupby(['traffic','ip']))
# print(f"UV:{uvlen}")
ip数目=date["ip"].value_counts().size
# print('独立IP的数目为：',ip数目)
# hourList=[]
# sortYList=[]
# dateList=date['access_time'].values.tolist()
# for s in dateList:
#    hourList.append(int(s[13:15]))
# sortXList = sorted(Counter(hourList).keys())
# for i in sortXList:
#    sortYList.append(Counter(hourList).get(i))
# x=sortXList
# y=sortYList
#
# line=(Line().set_global_opts(
#        tooltip_opts=opts.TooltipOpts(is_show=False),
#        xaxis_opts=opts.AxisOpts(type_="category",name="访问时间"),
#        yaxis_opts=opts.AxisOpts(
#            type_="value",
#            axistick_opts=opts.AxisTickOpts(is_show=True),
#            splitline_opts=opts.SplitLineOpts(is_show=True),
#            interval=1409,
#            name="访问人次",
#        ),
#    )
#
#    .add_xaxis(xaxis_data=x)
#    .add_yaxis(
#        series_name="访问趋势",
#        y_axis=y,
#        symbol="emptyCircle",
#        is_symbol_show=True,
#        label_opts=opts.LabelOpts(is_show=False),
#    )
# )
# line.render("访问趋势.html")
# direct = len(re.compile(r'www.chinamoocs.com').findall(date['url'].to_string()))
# engine = len(re.compile(r'.com').findall(date['url'].to_string()))-direct
# blank=0
# for s in date['url']:
#    if s=='-':
#        blank+=1
# other = len(date['url'])-direct-engine
#
# x_data=['直接访问','搜索引擎','其他链接']
# y_data=[direct,engine,other]
# c = (
#    Pie()
#    .add(
#        "",
#        [list(z) for z in zip(x_data, y_data)],
#        radius=["40%", "75%"],
#    )
#    .set_global_opts(
#        title_opts=opts.TitleOpts(title="访问来源占比"),
#        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
#    )
#    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}， {d}%"))
#    .render("访问来源占比.html")
# )
# google = len(re.compile(r'google.com').findall(date['url'].to_string()))
# sll =len(re.compile(r'so.com').findall(date['url'].to_string()))
# baidu =len(re.compile(r'baidu.com').findall(date['url'].to_string()))
# sogou =len(re.compile(r'www.sogou.com').findall(date['url'].to_string()))
# qq =len(re.compile(r'qq.com').findall(date['url'].to_string()))
# 
# x_data=['baidu','360','google','sogou','qq']
# y_data=[baidu,sll,google,sogou,qq]
# c = (
#    Pie()
#    .add(
#        "",
#        [list(z) for z in zip(x_data, y_data)],
#        radius=["40%", "75%"],
#    )
#    .set_global_opts(
#        title_opts=opts.TitleOpts(title="搜索引擎占比"),
#        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
#    )
#    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#    .render("搜索引擎.html")
# )

