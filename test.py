import mysql.connector as conn
mycon=conn.connect(host='localhost', user='root', passwd='tushar', database='project')

if mycon.is_connected():
    print("successfully connected to mysql database")