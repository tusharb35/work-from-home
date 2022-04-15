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


#======================1.FUNCTION FOR ATTENDANCE=================================



def attendance(a,s):
    s_t="select rollno,name from student1 where sec='{}' and class={} order by rollno".format(s,a)
    cursor.execute(s_t)
    data=cursor.fetchall()
    for a in data:
        print(a)
        
    count=cursor.rowcount
    for i in range(1,count):
        att=input("Enter P if present and A for adsent FOR ROLL NUMBER "+str(i)+" :- ")
        if att=='P':
            st="update student2,student1 set attendance=attendance+1 where sec='{}' and class={} and rollno={} and student1.admno=student2.admno".format(s,a,i)
            cursor.execute(st)
            mycon.commit()
        else:
            st2="update student2,student1 set attendance=attendance+0 where sec='{}' and class={} and rollno={} and student1.admno=student2.admno".format(s,a,i)
            cursor.execute(st2)
            mycon.commit()
            
#=====================2.FUNCTION FOR ADDING NEW STUDENT==========================
            
            

def addstudent(name,adno,clas,sec,rn):
    cursor.execute("insert into student1 values({},'{}',{},'{}',{})").format(adno,name,clas,sec,rn)
    mycon.commit()
    cursor.execute("insert into student2 values({})").format(adno)
    mycon.commit()
    
    
#====================3.FUNCTION FOR UPDATING NAME================================
    
    

def upname(na2,admo):
    cursor.execute("update student1 set name='{}' where admno={}").format(na2,admo)
    mycon.commit()
    
    

#====================4.FUNCTION F0R UPDATING CLASS===============================
    
    
def updclas(clas,admo):
    cursor.execute("update student1 set class={} where admno={}").format(clas,admo)
    mycon.commit()
    
    

#====================5.FUNCTION FOR UPDATING SECTION=============================
    
    
def upsec(se,admo):
    cursor.execute("update student1 set sec='{}' where admno={}").format(se,admo)
    mycon.commit()
    

#===================6.FUNCTION FOR UPDATING ADMISSION NUMBER===================
    
    
def upnum(admo1,admo2):
    cursor.execute("update student1 set admno={} where admno={}").format(admo2,admo1)
    mycon.commit()
    cursor.execute("update student2 set admno={} where admno={}").format(admo2,admo1)
    mycon.commit()
    

#==================7.FUNCTION FOR DISPLAY ATTENDENCE OF A PARICULAR STUDENT======
            
            
def disatt(name,clas,sec):
    cursor.execute("select rollno,name,attendence from student1,student2 where name={} and class={} and sec={} and admo={} and student1.admno=student2.admno").format(name,clas,sec,admo)            
    data=cursor.fetchall()
    for i in data:
        print(i)        


#==================8.FUNCTION FOR DELETING DATA OF A STUDENT=======================



def deletingdata(adno):
    cursor.execute("delete ADMNO,NAME,CLASS,SEC,ROLLNO from student1 where admno={}").format(adno)
    mycon.commit()
    
#=================9.FUNCTION FOR TO DISPLAY ALL DATA=============================


def display():
    cursor.execute("select * from student1,student2 where student1.admno=student2.admno")
    data=cursor.fetchall()
    for i in data:
        print(i)

#=================10.FUNCTION FOR EXIT=========================================
        #=========IN THE MAIN PROGRAM==================



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
    attendance(a,s)
    
    print('NO ROLL NUMBER ARE LEFT')
     
     
#================2.ADDING NEW STUDENT=================


if ch==2:
    print('''
                 ADDING NEW STUDENT            ''')
    name=input("ENTER THE NAME :- ")
    adno=eval(input('ENTER THE ADMISSION NUMBER :- '))
    clas=input('ENTER THE CLASS :- ')
    sec=input('ENTER THE SECTION :- ')
    rn=eval(input('ENTER THE ROLL NUMBER :- '))
    addstudent(name,adno,clas,sec,rn)
    
    print('STUDENT HAS BEEN SUCCESFULLY ADDED ')
    
    
    

#===============3.UPDATING NAME==========================
    
    
if ch==3:
    print('''
                 UPDATING NAME           ''')
    na1=input('ENTER THE PRVIOUS NAME OF THE STUDENT :- ')
    admo=eval(input('ENTER THE ADMISSION NUMBER OF THE STUDENT:- '))
    na2=input('ENTER THE NEW NAME TO BE UPDATE :- ')
    upname(na2,admo)
    
    print('STUDENT NAME HAS BEEN SUCCESFULLY UPDATED ')
    
    
    
    
#=============4.UPDATING CLASS==========================
    
    
if ch==4:
    print('''
                 UPDATING CLASS           ''')
    name=input('ENTER THE NMAE OF SUDENT :- ')
    admo=eval(input('ENTER THE ADMISSION NUMBER OF THE STUDENT:- '))
    clas=eval(input('ENTER THE NEW CLASS OF STUDENT :- '))
    clss(clas,admo)
    
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
    
    
    
    
#=============6.UPDATING ADMISSION NUMBER================



if ch==6:
    print('''
                UPDATING ADMISSION NUMBER      ''')
    
    admo1=eval(input('ENTER THE OLD ADMISSION NUMBER OF THE STUDENT :- '))
    name=input('ENTER THE NAME OF STUDENT :- ')
    clas=eval(input('ENTER THE CLASS OF THE STUDENT :- '))
    admo2=eval(input('ENTER THE NEW ADMISSION NUMBER OF THE STUDENT :- '))
    upnum(admo1,admo2)
    
    print('STUDENT ADMISSION NUMBER HAS BEEN SUCCESFULLY UPDATED ')
    
    
#===========7.TO DISPLAY ATTENDENCE OF A PARICULAR STUDENT======
    
    
if ch==7:
    print('''
             TO DISPLAY ATTENDENCE OF A PARICULAR STUDENT  ''')
    name=input('ENTER THE NAME OF THE STUDENT :- ')
    clas=eval(input('ENTER THE CLASS OF THE STUDENT :- '))
    sec=input('ENTER THE SECTION OF THE STUDENT :- ')
    admo=eval(input('ENTER THE ADMISSION NUMBER OF THE STUDENT :- '))
    disatt(name,clas,sec)
    
    

#===========8.DELETING DATA OF A STUDENT========================
    

if ch==8:
    print('''
              TO DELETING DATA OF ''')
    name=input('ENTER THE NAME OF THE STUDENT :- ')
    admo=eval(input('ENTER THE ADMISSION NUMBER OF THE STUDENT :- '))
    deletingdata(admo)
    

#===========9.DISPLAYING ALL DATA================================
    

if ch==9:
    print('''
                DISPLAYING ALL DATA  ''')
    display()


