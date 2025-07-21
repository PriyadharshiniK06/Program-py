import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',password='root',database='first')
mycursor=a.cursor()
#sql = "UPDATE F SET address = 'Canyon 123' WHERE address = 'Valley 345'"
'''sql = "UPDATE F SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
a.commit()
print(mycursor.rowcount, "record(s) affected")'''


#mycursor.execute("SELECT * FROM F limit 5")
mycursor.execute("SELECT * FROM F limit 5 offset 2")
myresult = mycursor.fetchall()
for x in myresult:
      print(x)

'''mycursor.execute(sql)
a.commit()
print(mycursor.rowcount, "record(s) affected")'''
#mycursor.execute('CREATE TABLE F(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(670),ADDRESS VARCHAR(670))')
#b="insert into F(NAME,ADDRESS)values(%s,%s)"


'''c=[
    ('RIYA','HIGHWAY 21'),
    ('PRIYA','LILLYGARDEN 67'),
    ('HISHA','HIGHWAY 56'),
    ('HARI','LOTUSGARDEN 89'),
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
     ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
   ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
   ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
   ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
   ('Chuck', 'Main Road 989'),
   ('Viola', 'Sideway 1633')

   ] '''

'''mycursor.executemany(b,c)
a.commit()
print(mycursor.rowcount,"was inserted")'''


