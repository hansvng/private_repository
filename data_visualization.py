#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: hansvng

# 柱状图-Bar

from pyecharts.charts import Bar
from pyecharts import options as opts
# 设置行名
bar = Bar()
bar.add_xaxis(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

# 设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# 设置柱状图的标题
bar.set_global_opts(title_opts=opts.TitleOpts(title="一年的降水量与蒸发量"))
# 添加柱状图的数据
bar.add_yaxis("降水量", data1)
bar.add_yaxis("蒸发量", data2)

# 生成本地文件（默认为.html文件）
bar.render()