import sqlite3 as conn
mycon=conn.connect('project.db')

cursor=mycon.cursor()

#cursor.execute("select curdate()")
#date=cursor.fetchall()

#print("TODAY DATE IS ",date)


#===========Creating table for the operations======

cursor.execute("CREATE TABLE if not exists student1(ADMNO int(4) primary key ,NAME varchar(30) not null,CLASS int(2) not null,SEC char(1) not null,ROLLNO int(2))")

cursor.execute("CREATE TABLE if not exists student2(ADMNO int(4) primary key,ATTENDENCE int(11))")
             
             
ch=eval(input("ENTER THE NUMBER OF OPERATION YOU WANT TO DO :- "))

#================2.ADDING NEW STUDENT=================

cursor.execute("select * from student1")
data=cursor.fetchall()
for a in data:
    print(a)
cursor.execute("select * from student2")
data1=cursor.fetchall()
for a in data1:
    print(a)


if ch==7:
    print('''
             TO DISPLAY ATTENDENCE OF A PARICULAR STUDENT  ''')
    name=input('ENTER THE NAME OF THE STUDENT :- ')
    clas=eval(input('ENTER THE CLASS OF THE STUDENT :- '))
    sec=input('ENTER THE SECTION OF THE STUDENT :- ')
    admo=eval(input('ENTER THE ADMISSION NUMBER OF THE STUDENT :- '))
    st="select rollno,name,attendence,ADMNO from student1,student2 where name='{}' and class={} and sec='{}' and student1.ADMNO=student2.ADMNO".format(name,clas,sec)
    cursor.execute(st)
    date=cursor.fetchall()
    for i in data:
        print(i)