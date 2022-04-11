import mysql.connector as conn
mycon=conn.connect(host='localhost', user='root', passwd='tushar', database='project')
cursor=mycon.cursor()
cursor.execute("select curdate()")
date=cursor.fetchall()
print(date)
