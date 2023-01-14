import pymysql as sql
def getConnection():
    conn = sql.connect(host='localhost',port=3307,user='root',database='employee_info')
    return conn
conn = getConnection()
cur = conn.cursor()
query = 'SELECT * FROM EMPLOYEE'
cur.execute(query)
k = cur.fetchall()
for i in k:
    print(i)
print(k)
conn.commit()
conn.close()