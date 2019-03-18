html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('#container .list li'))  #css选择器 得到所有li子节点
print(type(doc('#container .list li')))

# 查找子节点
items = doc('.list') #选取url
lis = items.find('li') #选择内部的li   find查找范围是节点的所有子孙节点

# 如果只想查找子节点   可以用children方法
lis2 = items.children('.active')
print(lis2)

# 父节点
contain = items.parent()  # 上一级
#print(contain)

# 祖先节点
parents = lis2.parents()  # 返回2个  id='container'  class='list'
print(parents)
print(parents('#container'))


#兄弟节点
li = doc('.item-0.active')
print(li)
print(li.siblings()) #得到所有同级节点
print(li.siblings('.active')) #加入css选择筛选
