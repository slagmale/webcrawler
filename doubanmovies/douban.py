import requests
import re
import json
from requests import RequestException
import time

# 得到一个页面的文本
def get_one_page(url):
    try:
        headers = {
            'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
        }
        html = requests.get(url)
        if html.status_code == 200:
            return html.text
        return None
    except RequestException:
        return None

# 解析文本得到信息
def parse_html(html):
    pattern = re.compile(
        '<div class="item">.*?<em.*?>(\d+).*?<img.*?src="(.*?)".*?class="title">(.*?)</span>.*?"v:average">(.*?)</span>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'rank': item[0],  # 排名
            'image': item[1],  # 电影封面
            'title': item[2],  # 电影名
            'score': item[3]  # 评分
        }

def write_to_file(content):
    with open('results.txt', 'a', encoding='utf-8') as f:
        # print(type(json.dumps(content))) # josn.dumps实现字典的序列化  将obj转换为str
        f.write(json.dumps(content,
                           ensure_ascii=False) + '\n')  # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
        # f.write(content) # TypeError: write() argument must be str, not dict

def main(offset):
    url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
    html = get_one_page(url)
    for item in parse_html(html):
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(i * 25)  # 页面规律 offset 由0-255分别对应 1-10页  实现分页爬
        time.sleep(1)
