import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',password='root',database='first')
mycursor=a.cursor()
#mycursor.execute('CREATE TABLE F(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(670),PLACE VARCHAR(900))')
b="insert into F(NAME,ADDRESS)values(%s,%s)"


c=[
    ('RIYA','HIGHWAY 21'),
    ('PRIYA','LILLYGARDEN 67'),
    ('HISHA','HIGHWAY 56'),
    ('HARI','LOTUSGARDEN 89'),
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652')
   ]

mycursor.executemany(b,c)

#mycursor.executemany(sql, val)
a.commit()
print(mycursor.rowcount, "was inserted.")
    
