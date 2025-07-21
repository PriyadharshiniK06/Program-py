import mysql.connector

a=mysql.connector.connect(host='localhost',user='root',password='root')
#print(a)
mycursor=a.cursor()
#mycursor.execute('CREATE DATABASE THEERROSE')
mycursor.execute('show databases')
for x in mycursor:
    print(x)
