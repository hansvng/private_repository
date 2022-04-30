#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: hansvng

# Rrequests库抓取图片
"""
import requests
url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Flib.nuist.edu.cn%2Fupload_files%2Farticle%2F7%2F1_20170424112251.jpg&refer=http%3A%2F%2Flib.nuist.edu.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1615690190&t=5c2c0c7700f96eadecb2bd75e5a9162b"
img01 = requests.get(url)
with open('/Users/hansvng/Downloads/aboutime.png', 'wb') as f:
    f.write(img01.content)
"""

# 正则表达式
"""
import re
a = "\d{2}st"
str1 = "teach12345student"
ret = re.search(a, str1)
print(ret)
"""

# 爬虫抓取网页内容
"""
import requests
from bs4 import BeautifulSoup
import time

headers={
    'User=Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
def get_info(url):
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text, 'html.parser')
    ranks=soup.select('span.pc_temp_num')
    titles=soup.select('div.pc_temp_songlist>ul>li>a')
    times=soup.select('span.pc_temp_tips_r>span')
    print("{:^10}\t{:^20}\t{:^25}\t{:^35}".format("排名","歌手","歌曲","时长"))
    for rank, title,time in zip(ranks,titles,times):
        data={
            "排名":"{:<8}".format(rank.get_text().strip()),
            "歌手":"{:<15}".format(title.get_text().split('-')[0],chr(12288)),
            "歌曲":"{:<20}".format(title.get_text().split('-')[1],chr(12288)),
            "时长":time.get_text().strip()
        }
        print(data)
if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-888.html'.format(str(i) for i in range(1,24))]
    for url in urls:
        get_info(url)
        time.sleep(1)
"""

# 访问百度翻译并输出翻译结果
'''
import requests
import json

url="https://fanyi.baidu.com/v2transapi?from=en&to=zh"
headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
word=input("请输入您要翻译的内容：")
data={
    'from': 'en',
    'to': 'zh',
    'query': 'word'
}

res=requests.post(url, data, headers)
# 获取响应数据：json()方法返回的是obj(如果确认响应数据是json类型的，才可以使用json())
dic_obj=res.json()

filename=word+'.json'
fp=open(filename,'w',encoding='utf-8')
json.dump(dic_obj, fp, ensure_ascii=False)

print('finish')
'''

# 批量爬取网页壁纸
import re
import time
import requests

def Picture_Download(url_img_path, img_title):
    file_name = img_title.replace('/', '').strip()
    try:
        result = requests.get(url_img_path.strip())
    except:
        print(url_img_path, 'Download failed')
    else:
        if result.status_code == 200:
            File = open(file_name + '.jpg', 'wb')
            File.write(result.content)
            File.close()
def Img_Url(url):
    result = requests.get(url)
    result.encoding = 'gbk'
    all = re.findall(r'<img src=".*?" alt=".*?"/>', result.text)
    for item in all:
        print(item[0], item[1])
        Picture_Download(item[0], item[1])
def main():
    for i in range(1,74):
        if i ==1:
            Img_Url(r'http://www.netbian.com/weimei/index.htm')
        else:
            Img_Url(r'http://www.netbian.com/weimei/index_%d.htm' % i)
            time.sleep(2)
if __name__ == '__main__':
    main()