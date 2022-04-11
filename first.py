#========connecting database==============
import mysql.connector as conn
mycon=conn.connect(host='localhost', user='root', passwd='tushar', database='project')
cursor=mycon.cursor()

#==================MAIN PROGRAM====================
print('''
      
      _____________________________________________________
                MENU
      ----------------------------------------------------- 
              
         1.ATTENDECE
         
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
ch=eval(input("ENTER THE NUMBER OF OPERATION YOU WANT TO DO :-"))

#==========1.ATTENDENCE==================================
if ch==1:
    a=eval(input("ENTER THE CLASS :- "))
    s=input("ENTER THE SECTION :- ")
    s_t="select rollno,name from student1 where class={} order by rollno".format=(a)
    cursor.execute(s_t)
    data=cursor.fetchall()
    for a in data:
        print(a)