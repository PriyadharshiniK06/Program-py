import mysql.connector
#create database ('mysql.connector','root','employee')
a=mysql.connector.connect(host='localhost',user='root',password='root',database='employee')


mycursor=a.cursor()
mycursor.execute('CREATE TABLE EMPLOYEES ('ID' INT(10),'NAME' VARCHAR(25),'DEPARTMENT' VARCHAR(34),'DOB' VARCHAR(56))')
print(mycursor)
                 
