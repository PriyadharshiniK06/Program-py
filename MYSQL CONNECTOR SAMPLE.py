import mysql.connector

a=mysql.connector.connect(host='localhost',user='root',password='root',database='THEERROSE')

mycursor=a.cursor()

mycursor.execute('CREATE TABLE sample(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(670),address VARCHAR(560)')
