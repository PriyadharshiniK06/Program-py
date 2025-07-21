import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',password='root',database='Employee_Details')
mycursor=a.cursor()
#mycursor.execute('create database Employee_Details')
#print(mycursor)
#print(a) 
#mycursor.execute('create table A(ID varchar(45),NAME VARCHAR (100),DEPARTMENT VARCHAR(100),DOB VARCHAR(100))')
#print(mycursor)
'''sql='insert into A(ID,NAME,DEPARTMENT,DOB) values (%s,%s,%s,%s)'
val=[
    ('134567','Roshini','CSE','12-03-04'),
    ('145678','Harshini','ECE','13-05-05'),
    ('154326','Dharshini','EEE','24-03-06'),
    ('167889','Sruthi','FT','10-02-04'),
    ('123890','Sweetha','ROBOTICS','20-06-04'),
    ('145890','Deepika','EEE','15-07-05'),
    ('189345','Lavanya','CSE','16-08-06')
]
mycursor.executemany(sql,val)    
a.commit()
print(mycursor.rowcount ,'was inserted')'''
#for i in mycursor:
 #   print(i)
#mycursor.execute(sql,val) 
mycursor.execute('select * from A')
myresult=mycursor.fetchall()
print(myresult) 
'''for x in myresult:
    print(x)'''
#c='delete from '   
    
#print(myresult)   