from lxml import etree

# XPath 提供了很多节点轴选择方法，英文叫做 XPath Axes，包括获取子元素、兄弟元素、父元素、祖先元素等等
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*') # 可以获取所有祖先节点，其后需要跟两个冒号，然后是节点的选择器，使用了 *，表示匹配所有节点
print(result)
result = html.xpath('//li[1]/ancestor::div') # 在冒号后面加了 div，这样得到的结果就只有 div 这个祖先节点了。
print(result)
result = html.xpath('//li[1]/attribute::*') #  attribute 轴，可以获取所有属性值，其后跟的选择器还是 *，这代表获取节点的所有属性，返回值就是 li 节点的所有属性值。
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]') #  child 轴，可以获取所有直接子节点，在这里我们又加了限定条件选取 href 属性为 link1.html 的 a 节点。
print(result)
result = html.xpath('//li[1]/descendant::span') # 可以获取所有子孙节点，这里我们又加了限定条件获取 span 节点，所以返回的就是只包含 span 节点而没有 a 节点。
print(result)
result = html.xpath('//li[1]/following::*[2]') #  following 轴，可以获取当前节点之后的所有节点，这里我们虽然使用的是 * 匹配，但又加了索引选择，所以只获取了第二个后续节点。
print(result)
result = html.xpath('//li[1]/following-sibling::*') # following-sibling 轴，可以获取当前节点之后的所有同级节点，这里我们使用的是 * 匹配，所以获取了所有后续同级节点。
print(result)