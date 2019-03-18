import csv

with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile) # 初始化一个写入对象
    # 传入每行数据
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])


with open('data2.csv','w') as csvfile:
    writer = csv.writer(csvfile,delimiter=' ') # 指定列与列之间的分隔符
    # 写入多行
    writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])
