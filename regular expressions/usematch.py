import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
'''
^Hello  以Hello开头
\s 匹配空字符
\d 匹配数字[0-9]
\w 匹配字母、数字 下划线

match 方法第一个从参数 正则表达式  第二个参数传入要匹配的字符串
从头开始匹配
'''
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())  # 匹配到的内容
print(result.span())  # 匹配到的字符串在原字符串的位置范围

# 匹配目标
content2 = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('^Hello\s(\d+)\s\w{10}', content2)  # 使用括号将想提取的子字符串括起来  （）标记一个子表达式的开始和结束
print(result2.group())
print(result2.group(1))  # 输出第一个被()包围的匹配结果  如果后面还有匹配到的内容  依次用group(2) group(3)

# 通用匹配 .*
# .匹配任意字符（除了换行符）  *表示匹配前面的字符无限次    $匹配一行字符串的结尾
result3 = re.match('^Hello.*Demo$', content)
print(result3.group())

# 贪婪与非贪婪
result4 = re.match('^Hello.*(\d+).*Demo$', content2)
print(result4.group(1))  # 输出7  why?
# 原因: 贪婪匹配  .* 会匹配尽可能多的字符  \d+ 至少一个数字但没有指定有多少数字 这里把123456都匹配了  给\d+留下一个满足条件的7

result5 = re.match('^Hello.*?(\d+).*Demo$', content2)
print(result5.group(1))  # .*? 非贪婪匹配   匹配到Hello后的空字符  再往后就是数字了  交给\d+匹配后面的数字  输出1234567

content3 = 'http://weibo.com/comment/kEraCN'
result6 = re.match('^http.*?comment/(.*?)', content3)
result7 = re.match('^http.*?comment/(.*)', content3)
print(result6.group(1))  # 如果要匹配的结果在字符串结尾  .*？就有可能匹配不到任何内容
print(result7.group(1))

#  修饰符
content4 = '''Hello 1234567 World_This is
 a Regex Demo'''
result8  = re.match('^He.*?(\d+).*?Demo$',content4,re.S)  # re.S 使.匹配包括换行符在内的所有字符
print(result8.group(1))

