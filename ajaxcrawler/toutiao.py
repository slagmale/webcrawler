import requests
from urllib.parse import urlencode
import re
import os
from requests import codes
from hashlib import md5
from multiprocessing.pool import Pool

'''
爬取今日头条街拍
'''


def get_page(offset):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    # 观察headers中请求的地址
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            # 除去那些不包括图片和标题的item  这些item有cell_type
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                big_image = re.sub('list', 'large', image.get('url'))
                yield {
                    # 图片链接改为获取大图片
                    'image': big_image,
                    'title': title
                }


def save_image(item):
    # os.path.sep  /分隔符
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'))
        if codes.ok == resp.status_code:
            # 图片文件名  使用其内容的MD5值 避免重复
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(), file_suffix='.jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('download image path is %s' % file_path)
            else:
                print('already download')
    except requests.ConnectionError:
        print('fail to save image,item %s' % item)



def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        save_image(item)

GROUP_START = 0
GROUP_END = 6

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()