# 1.文件上传
import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)  # 文件上传部分会单独有一个files字段标识

# 2.Cookies
r2 = requests.get('https://www.baidu.com')
print(r2.cookies)
for key, value in r2.cookies.items():
    print(key + '=' + value)

# 可以用cookie来维持我们的登录状态  登录知乎将Headers中的Cookie内容复制下来 添加到headers
headers = {
    'Cookie':
        '_zap=43795ccd-2f81-4dd7-ad68-7b0bdd98054e; _xsrf=jCRRwYsEknMuBEWeKotN4L5xNPF8q6oi; '
        'd_c0="ACDkojJ42g6PTmUfoaRbPMxjBIXZ3zCma08=|1547959410"; '
        'z_c0="2|1:0|10:1548938354|4:z_c0|92:Mi4xWEdNUUJBQUFBQUFBSU9TaU1uamFEaVlBQUFCZ0FsVk5janBBWFFEQzhk'
        'S2dkTzY5YTk1YkdvU2ZaWFVvVHpkWS1n|10818f5ac11521a0d31a7b15344ad021effd70addea81675236a6dd5702e5'
        '133"; tst=r; q_c1=99cac828b0214a718387d4b2cecd6988|1548938630000|1548938630000; __utmc=51854390;'
        ' __utmv=51854390.100--|2=registration_date=20170205=1^3=entry_date=20170205=1; _'
        '_utma=51854390.604952723.1548938631.1548938631.1550148473.2; __utmz=51854390.155'
        '0148473.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/tellmewhy-33/collections; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
r3 = requests.get('http://www.zhihu.com', headers=headers)
print(r3.text)

# 3.会话维持  ???
requests.get('http://httpbin.org/cookies/set/number/12345')  # 设置一个cookie number=12345
r4 = requests.get('http://httpbin.org/cookies')
print(r4.text)  # cookies为空

# 使用session
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/12345')
r5 = s.get('http://httpbin.org/cookies')
print(r5.text)

# 4.SSL证书认证
# 使用verify参数控制是否检查此证书
r6 = requests.get('https://www.12306.cn')
print(r6.status_code)

# 5.代理
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'https://10.10.1.10:1028',
}
requests.get('https://www.taobao.com', proxies=proxies)

# SOCKS协议代理

# 6.超时设置
#r8 = requests.get('https://www.taobao.com', timeout=0.1)

# 7.身份认证
# 自带身份认证
from requests.auth import HTTPBasicAuth

r9 = requests.get('http://localhost:5000', auth=('username', 'password'))  # 传入一个元组 默认使用HTTPBasicAuth这个类认证

# 8.Prepared Request
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
s = Session()
# 构造Request对象
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)