import mysql.connector

a=mysql.connector.connect(host='localhost',user='root',password='root',database='first')
mycursor=a.cursor()
#mycursor.execute('select * from I')
#b='select * from I where ADDRESS like"%way%"'
'''b='delete from I where ADDRESS= %s'
c=('YELLOW GARDEN 2',)'''
#b='drop table if exists I'
sql = "UPDATE I SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

#mycursor.execute(b)
#b='select * from I order by NAME'
#b='select * from I order by NAME desc'
#b='delete from I where address="HIGHWAY 21"'
#mycursor.execute(b,c)
#a.commit()
#print(mycursor.rowcount,"record(s) deleted")
#mycursor.execute('select NAME,ADDRESS from I')
#mycursor.execute('select * from I')
'''myresult=mycursor.fetchall()
print(myresult)
for x in myresult:
    print(x)
'''
#mycursor.execute('CREATE TABLE I(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(670),ADDRESS VARCHAR(670))')
#b="insert into I(NAME,ADDRESS)values(%s,%s)"

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

   ] 
mycursor.executemany(b,c)
a.commit()
print(mycursor.rowcount,"was inserted")
''''''


''''''
mycursor.execute('create database first')
mycursor.execute('show databases')'''
'''
for i in mycursor:
    print(i)'''
'''c=('RIYA','HIGHWAY 21')
mycursor.execute(b,c)
a.commit()
print("1 record inserted ID: ",mycursor.lastrowid)'''                         
