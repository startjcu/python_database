import MySQLdb

# 获取连接
try:
    conn = MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        password='111111',
        db='python',
        port=3306,
        charset='utf8'
    )
except MySQLdb.Error as e:
    print('Error: %s' % e)
# 获取数据
cursor = conn.cursor()
cursor.execute('SELECT * FROM students')
rest = cursor.fetchone()
print(rest)

# 关闭连接
conn.close()
