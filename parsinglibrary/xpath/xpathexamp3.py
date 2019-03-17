# 按序选择

'''
有时候我们在选择的时候可能某些属性同时匹配了多个节点，但是我们只想要其中的某个节点，如第二个节点，或者最后一个节点
可以利用中括号传入索引的方法获取特定次序的节点
'''
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)

'''
XPath 中提供了 100 多个函数，包括存取、数值、字符串、逻辑、节点、序列等处理功能，
具体所有的函数作用可以参考：http://www.w3school.com.cn/xpath/xpath_functions.asp。
'''
