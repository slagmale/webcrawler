# 使用sub来修改文本

import re
content = '54aK54r5iR54x5l2g'
# \d+ 匹配所有数字  ''赋值为空  content原字符串
content = re.sub('\d+','',content)
print(content)


# compile 将正则编译成正则表达式对象  以便在后面的匹配复用
content1 = '2017-5-22 12:23'
content2 = '2017-5-22 04:23'
content3 = '2017-5-22 21:23'
pattern = re.compile('\d{2}:\d{2}')
r1 = re.sub(pattern,'',content1)
r2 = re.sub(pattern,'',content2)
r3 = re.sub(pattern,'',content3)
print(r1)
print(r2)
print(r3)