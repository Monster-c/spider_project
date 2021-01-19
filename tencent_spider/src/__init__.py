# -*- coding =utf-8 -*-
# @Time : 2021/1/19 10:46
# @Author : 曹显伟
# @File __init__.py.py
# @Software: PyCharm

import requests
from lxml import etree

base_url = "https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=0&limit=20&strategy=1&ext={%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}

resp = requests.get(base_url)
if resp.status_code == 200:
    print("Successful!!")
else:
    print("Error!!!")

'''@return list of titles, urls'''
def pase_json(_json):
    data = _json['data']
    list = data['list']
    # 保存新闻标题
    titles = []
    # 保存新闻地址
    news_urls = []
    for news in list:
        titles.append(news['title'])
        news_urls.append(news['url'])
    return titles, news_urls

'''将解析出的新闻地址进一步解析'''
def get_news(titles,urls):
    news = []
    # 创建一个session方便跨页面同时减少访问次数，方便狗住
    sessions = requests.session()
    sessions.headers = headers

    for url in urls:
        response = sessions.get(url)
        html = response.text
        #将html文本解析成节点元素
        soup = etree.HTML(html)
        temp = soup.xpath('//div[@class="content clearfix"]/div[@class="content-article"]/p/text()')
        #type（temp）为list，转化为str
        text = ''.join(temp)
        news.append(text)

        details = tuple(zip(titles,news))

    return details

if __name__ == "__main__":
    titles, urls = pase_json(resp.json())
    details = get_news(titles,urls)
    with open('news.txt', 'w',encoding='utf-8') as f:
        for i in details:
            for j in i:
                f.write(j)

