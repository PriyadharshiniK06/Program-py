import mysql.connector

a=mysql.connector.connect(host='localhost',user='root',password='root',database='SECOND')

'''mycursor=a.cursor()

mycursor = a.cursor()
mycursor.execute("CREATE DATABASE SECOND")'''

#mycursor = a.cursor()

#mycursor.execute('CREATE TABLE USER(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), FAVORITE VARCHAR(255))')

'''mycursor = a.cursor()
sql = "INSERT INTO USER (name, FAVORITE) VALUES (%s, %s)"
val = [
         ('JOHN', '154'),
         ('PETER', '154'),
         ('AMY', '155'),
         ('Hannah','' ),
         ('Sandy','' )
      ]
mycursor.executemany(sql, val)

a.commit()
print(mycursor.rowcount, "was inserted.")'''


'''mycursor=a.cursor()
#mycursor.execute('create table productss(id varchar(450) primary key, name varchar(560))')
#mycursor=a.cursor()
sql = "INSERT INTO productss(id,name) VALUES (%s,%s)"
val = [
         ('154','chocolate heaven'),
         ('155','tasty lemons'),
         ('156','vannilla dreams')
         
      ]
mycursor.executemany(sql,val)

a.commit()
print(mycursor.rowcount, "was inserted.")'''

mycursor = a.cursor()
#sql = "SELECT USER.name AS USER, productss.name AS FAVORITE FROM USER JOIN productss ON USER.FAVORITE= productss.id"

#sql="SELECT USER.name AS USER, productss.name AS FAVORITE FROM USER LEFT JOIN productss ON USER.FAVORITE = productss.id"

#sql="select USER.name as USER, productss.name as FAVORITE from USER right join productss on USER.FAVORITE=productss.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
      print(x)
