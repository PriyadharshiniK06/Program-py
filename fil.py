import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',password='root',database='first')
mycursor=a.cursor()
mycursor.execute('SELECT * from A')
result=mycursor.fetchall()
for x in result:
    print(x)
