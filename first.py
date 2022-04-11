import sqlite3 as conn
mycon=conn.connect('project.db')

cursor=mycon.cursor()

st="select curdate()"

cursor.execute(st)
date=cursor.fetchall()

print("TODAY DATE IS ",date)


#===========Creating table for the operations======

cursor.execute("CREATE TABLE if not exists student1(ADMNO int(4) primary key ,NAME varchar(30) not null,CLASS int(2) not null,SEC char(1) not null,ROLLNO int(2))")

cursor.execute("CREATE TABLE if not exists student2(ADMNO int(4) primary key,ATTENDENCE int(11))")



#==================MAIN PROGRAM====================


print('''
          
          _____________________________________________________
                    MENU
          ----------------------------------------------------- 
                  
             1.ATTENDACE
             
             2.ADDING NEW STUDENT (NAME/CLASS/SECTION/ADMISSION 
               NUMBER FOLLOWING DATA SHOULD ENTER TOGETHER)
             
             3.UPDATING NAME
             
             4.UPDATING CLASS
             
             5.UPDATING SECTION
             
             6.UPDATING ADMISSION NUMBER
             
             7.TO DISPLAY ATTENDENCE OF A PARTICULAR STUDENT 
               (ADMN.IS REQUIRED)
               
             8.DELETING DATA OF STUDENT
             
             9.TO DISPLAY ALL DATA
             
             10.EXIT
           _____________________________________________________  ''')
             
             
ch=eval(input("ENTER THE NUMBER OF OPERATION YOU WANT TO DO :- "))

