from pyquery import PyQuery as pq
import requests

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# 字符串初始化
doc = pq(html)
print(doc('li'))

# url初始化
# Pyquery会先请求这个url 然后用得到的Html内容进行初始化
doc2 = pq(url='http://cuiqingcai.com')
print(doc2('title'))
# 等同于下例
doc3 = pq(requests.get('http://cuiqingcai.com').text)
print(doc3('titled'))

#文件初始化
doc4 = pq(filename='demo.html')
