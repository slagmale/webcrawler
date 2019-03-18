import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)  #将字符串转换为Json对象   键值需要用双引号  不然会报错
print(data)
print(type(data))

print(data[0]['name'])
print(data[0].get('name'))

print(data[0].get('age')) #返回None
print(data[0].get('age',25)) #传入默认值25

# 输出Josn
with open('data.json', 'w', encoding='utf-8') as file:
    #indent缩进2个字符  ensure_ascii规定输出编码
    file.write(json.dumps(data, indent=2, ensure_ascii=False))