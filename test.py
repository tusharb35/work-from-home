import mysql.connector as conn
mycon=conn.connect(host='localhost', user='root', passwd='tushar', database='project')

# if mycon.is_connected():
#     print("successfully connected to mysql database")


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



#==========1.ATTENDANCE==================================



if ch==1:
    print('''           
                        ATTENDENCE                   ''')
    a=eval(input("ENTER THE CLASS :- "))
    s=input("ENTER THE SECTION :- ")
    st="select ROLLNO,NAME from student1 where class={} and sec='{}'".format(a,s)
    cursor.execute(st)
    data=cursor.fetchall()
    for I in data:
        print(I)
            
            
    count=cursor.rowcount
    for i in range(1,count):
        att=input("Enter P if present and A for adsent FOR ROLL NUMBER "+str(i)+" :- ")
        if att=='P':
            st1="update student2,student1 set attendance=attendance+1 where sec='{}' and class={} and rollno={} and student1.admno=student2.admno".format(s,a,i)
            cursor.execute(st1)
            cursor.execute("select curdate()")
        else:
            st2="update student2,student1 set attendance=attendance+0 where sec='{}' and class={} and rollno={} and student1.admno=student2.admno".format(s,a,i)
            cursor.execute(st2)
            
        print('NO ROLL NUMBER ARE LEFT')
        
        
        

#================2.ADDING NEW STUDENT=================
        
        
if ch==2:
    print('''
                 ADDING NEW STUDENT           ''' )
    name=input("ENTER THE NAME :- ")
    adno=eval(input('ENTER THE ADMISSION NUMBER :- '))
    clas=eval(input('ENTER THE CLASS :- '))
    sec=input('ENTER THE SECTION :- ')
    rn=eval(input('ENTER THE ROLL NUMBER :- '))
    attendence=0
    st="insert into student1 values({},'{}',{},'{}',{})".format(adno,name,clas,sec,rn)
    cursor.execute(st)
    mycon.commit()
    st1="insert into student2 values({},{})".format(adno,attendence)
    cursor.execute(st1)
    mycon.commit()


