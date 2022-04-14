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


