'''
xpath:XML PATH Language XML路径语言 它是一门在XML文档中查找信息的语言。
Xpath设计之初 是用来搜寻XML文档的  它同样适用于HTML文档的搜索
'''
'''
表达式	    描述
nodename	选取此节点的所有子节点
/	从当前节点选取直接子节点
//	从当前节点选取子孙节点
.	选取当前节点
..	选取当前节点的父节点
@	选取属性

例子： //title[@lang='eng']   选取所有名称为title  属性lang值为eng的节点
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
html = etree.HTML(text)  # 对html文本进行修正
result = etree.tostring(html)  # 输出修正后的代码  结果是bytes类型
print(result.decode('utf-8')) # 使用decode方法转化为字符串


html2 = etree.parse('./test.html',etree.HTMLParser())
result2 = etree.tostring(html)  # 输出修正后的代码  结果是bytes类型
print(result2.decode('utf-8')) # 使用decode方法转化为字符串

li = html.xpath('//li')
print(li)  # 返回列表  每一个元素都是Element对象

# 使用/或// 查找元素的子节点或子孙节点
a = html.xpath('//li/a')
a2 = html.xpath('//ul//a')


# 父节点
r = html.xpath('//a[@href="link4.html"]/../@class')
print(r)

# 属性匹配
sx = html.xpath('//li[@class="item-0"]')
print(sx)

# 文本获取
text = html.xpath('//li[@class="item-0"]/text()')
print(text)
#此 / 的含义是选取直接子节点，而此处很明显 li 的直接子节点都是 a 节点，文本都是在 a 节点内部的，
# 所以这里匹配到的结果就是被修正的 li 节点内部的换行符，因为自动修正的li节点的尾标签换行了。

# 想获取 li 节点内部的文本就有两种方式，一种是选取到 a 节点再获取文本，另一种就是使用 //
text2 = html.xpath('//li[@class="item-0"]/a/text()')
print(text2)
text3 = html.xpath('//li[@class="item-0"]//text()')# 这里是选取所有子孙节点的文本  包括li节点内部的换行符
print(text3)

# 获取属性
shuxing = html.xpath('//li/a/href')
print(shuxing)

