import requests

proxies = {
    'http':'https://119.123.177.169:9000'
}

r = requests.get('http://www.baidu.com',proxies=proxies)
r.encoding='utf-8'
print(r.text)