html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)  # 返回子节点列表
print(soup.p.children)  # 返回生成器类型
for i, child in enumerate(soup.p.children):
    print(i, child)

# 直接父节点
print(soup.span.parent)

# 所有父节点
print(list(enumerate(soup.a.parents)))
