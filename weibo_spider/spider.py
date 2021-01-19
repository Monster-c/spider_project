# -*- coding =utf-8 -*-
# @Time : 2021/1/19 17:35
# @Author : 曹显伟
# @File spider.py.py
# @Software: PyCharm

import requests
import json

url = "https://s.weibo.com/ajax/jsonp/gettopsug?uid=&ref=PC_topsug&url=https://weibo.com/?category=1760&Mozilla=Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64;%20rv:84.0)%20Gecko/20100101%20Firefox/84.0&_cb=STK_16110512812743"
headers= {'GET ':'/ajax/jsonp/gettopsug?uid=&ref=PC_topsug&url=https://weibo.com/?category=1760&Mozilla=Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64;%20rv:84.0)%20Gecko/20100101%20Firefox/84.0&_cb=STK_16110512812743%22 HTTP/1.1',
          'Host': 's.weibo.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
          'Accept-Encoding': 'gzip, deflate, br',
          'Connection': 'keep-alive',
          'Cookie': 'SUB=_2AkMo3iT6f8NxqwJRmfkVxG7qaIpzzwHEieKegtUhJRMxHRl-yT9jqk0atRB6A14KFRHYkpaQtYs5WyFEnYd04QzaZ8Id; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFI4yKRbwlGLXIDA8UpeYsw; UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=2301199146413.0312.1611023782196; ULV=1611023782199:1:1:1:2301199146413.0312.1611023782196:; login_sid_t=cd83bb5dc2d5b879bbfb4375842d0230; cross_origin_proto=SSL; _s_tentry=www.baidu.com; Apache=2301199146413.0312.1611023782196',
          'Upgrade-Insecure-Requests': '1',
          'DNT': '1',
          'Sec-GPC': '1',
          'Cache-Control': 'max-age=0'}



resp = requests.get(url,headers)

if resp.status_code == 200:
    print('successful!')
else:
    print('error!')


def get_json():
    # 由于发现目标json格式不标准，包含其他关键字，因此需要进行转换
    text = resp.text
    jsons = text.split('(')[1].split(')')[0]
    # 转换成python对象
    jsons = json.loads(jsons)

    return jsons


def parse_json(_json):
    for i in _json:
        print(i)

if __name__ == '__main__':
    jsons = get_json()
    parse_json(jsons)








