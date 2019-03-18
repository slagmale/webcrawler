import pymysql

'''
id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age)) # value值通过元组传入
    db.commit()
except:
    db.rollback()  # 发现异常就回滚
db.close()
'''

# 通用的插入方法  只需要提供动态的字典
db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
