import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',password='root',database='first')
mycursor=a.cursor()
#mycursor.execute('CREATE TABLE P(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(670),ADDRESS VARCHAR(900))')

'''b="insert into M (NAME,ADDRESS)values(%s,%s)"

c=[
    ('Richard', 'Sky st 331'),
   ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
   ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
   ('Chuck', 'Main Road 989'),
   ('Viola', 'Sideway 1633')
  ]

mycursor.executemany(b,c)

#mycursor.executemany(sql, val)
a.commit()
print(mycursor.rowcount, "was inserted.")

'''

sql = "SELECT \
F.NAME AS F, \
P.NAME AS ADDRESS \
FROM F \
JOIN F ON P.ADDRESS = F.NAME"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
     print(x)
