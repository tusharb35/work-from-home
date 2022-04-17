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

    
#===============3.UPDATING NAME==========================
    
    
if ch==3:
    print('''
                 UPDATING NAME           ''')
    na1=input('ENTER THE PRVIOUS NAME OF THE STUDENT :- ')
    admo=eval(input('ENTER THE ADMISSION NUMBER OF THE STUDENT:- '))
    na2=input('ENTER THE NEW NAME TO BE UPDATE :- ')
    st="update student1 set name='{}' where admno={} and name='{}' ".format(na2,admo,na1)
    cursor.execute(st)
    mycon.commit()
    
    print("UPDATE SUCCESSFULLY THE NAME ",na1)
    
   
#=============4.UPDATING CLASS==========================
    
    
if ch==4:
    print('''
                 UPDATING CLASS           ''')
    name=input('ENTER THE NMAE OF SUDENT :- ')
    admo=eval(input('ENTER THE ADMISSION NUMBER OF THE STUDENT:- '))
    clas=eval(input('ENTER THE NEW CLASS OF STUDENT :- '))
    updclas(clas,admo)
    
    print('STUDENT CLASS HAS BEEN SUCCESFULLY UPDATED ')
    
    

#==============5.UPDATING SECTION======================
    
    
if ch==5:
    print('''
                   UPDATING SECTION
        (*Admission NAME and SECTION of the student is MENDETORY)   ''')
    admo=eval(input('ENTER THE ADMISSION NUMBER OF THE STUDENT :- '))
    name=input('ENTER THE NAME OF THE STUDENT :- ')
    clas=input('ENTER THE CLASS OF THE STUDENT :- ')
    se=eval(input('ENTER THE NEW SECTION OF THE STUDENT :- '))
    upsec(se,admo)
    
    print('STUDENT SECTION HAS BEEN SUCCESFULLY UPDATED ')
    
    
    
    