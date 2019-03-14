# get请求
import requests

r = requests.get('http://www.baidu.com')
print(r.text)

response = requests.get('http://httpbin.org/get')
print(response.text)


response2 = requests.get('http://httpbin.org/get?name=peter&age=18')
print(response2.text)

data = {
    'name':'peter',
    'age':18
}
response3 = requests.get('http://httpbin.org/get',params=data)
print(response3.text)

# 抓取二进制数据
r = requests.get('https://github.com/favicon.ico') # 这里我们抓取Github站点图标
with open('favicon.ico','wb') as f:    # 向文件写入二进制数据
    f.write(r.content)

# 添加headers
# 因为有些网站不添加headers不能正常请求  比如知乎
    r2 = requests.get('https://www.zhihu.com/explore')
    print(r2.text)  # 返回400  表示服务器不能解析该请求

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    r3 = requests.get('https://www.zhihu.com/explore',headers=headers)
    print(r3.text)


# post请求
data = {
    'name':'peter',
    'age':18
}
r7 = requests.post('http://httpbin.org/post',data=data)
print(r7.text)

#响应
r8 = requests.get('https://www.jianshu.com',headers=headers)
print(r8.status_code) #状态码
print(r8.headers) # 响应头
print(r8.cookies) # cookies
print(r8.url)
print(r8.history)