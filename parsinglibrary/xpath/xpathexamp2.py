from lxml import etree
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result)

# 属性多值匹配
# contains() 方法，第一个参数传入属性名称，第二个参数传入属性值，这样只要此属性包含所传入的属性值就可以完成匹配了。
result2 = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result2)

# 多属性匹配
text2 = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html2 = etree.HTML(text2)
result3 = html2.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result3)
