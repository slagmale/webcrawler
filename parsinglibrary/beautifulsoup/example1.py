from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')  # 自动更正格式
print(soup.prettify())  # 以标准的缩进格式输出
print(soup.title)  # title节点
print(type(soup.title))  # bs4.element.Tag类型  有一些属性比如string
print(soup.title.string)  # 输出title节点的文本内容
print(soup.head)
print(soup.p)  # 若有多个P 只返回第一个匹配的节点

print(soup.p.name)  # name属性获取节点名称

# 获取属性
print(soup.p.attrs)  # 返回字典  属性+属性值
print(soup.p.attrs['name'])

# 获取属性简写
print(soup.p['class'])  # class可能有多个  返回列表
print(soup.p['name'])  # name唯一 返回字符串

# 获取内容
print(soup.p.string)
