import pymysql

# 声明Mysql连接对象
db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
# 获得操作游标
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
# 得到第一条数据
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()
