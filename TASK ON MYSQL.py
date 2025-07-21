mysql> create database task on mysql;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'on mysql' at line 1
mysql> create database taskonmysql;
Query OK, 1 row affected (0.01 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| data1              |
| information_schema |
| mysql              |
| performance_schema |
| sdt                |
| singleline         |
| singlelinequery    |
| sys                |
| taskonmysql        |
+--------------------+
9 rows in set (0.01 sec)

mysql> show taskonmysql;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'taskonmysql' at line 1
mysql> use taskonmysql;
Database changed
mysql> create table table(SNO int(20), NAME varchar(20),PNAME varchar(28),PRICE int(15),PNO varchar(29));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'table(SNO int(20), NAME varchar(20),PNAME varchar(28),PRICE int(15),PNO varchar(' at line 1
mysql> create table table(SNO int(20), NAME varchar(20),PNAME varchar(28), PRICE int(15), PNO varchar(29));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'table(SNO int(20), NAME varchar(20),PNAME varchar(28), PRICE int(15), PNO varcha' at line 1
mysql> create table product(SNO int(20), NAME varchar(20),PNAME varchar(28), PRICE int(15), PNO varchar(29));
Query OK, 0 rows affected, 2 warnings (0.06 sec)

mysql> desc product;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| SNO   | int         | YES  |     | NULL    |       |
| NAME  | varchar(20) | YES  |     | NULL    |       |
| PNAME | varchar(28) | YES  |     | NULL    |       |
| PRICE | int         | YES  |     | NULL    |       |
| PNO   | varchar(29) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

mysql> insert into product values(1000,'PRIYA','lenovo',10000,1345678905);
Query OK, 1 row affected (0.02 sec)

mysql> insert into product values(1500,'RIYA','printer',15000,1335668817);
Query OK, 1 row affected (0.01 sec)

mysql> insert into product values(2000,'LIRA','lenovo',20000,1345678875);
Query OK, 1 row affected (0.02 sec)

mysql> insert into product values(2500,'LUSIA','printer',25000,1455677876);
Query OK, 1 row affected (0.01 sec)

mysql> insert into product values(3000,'SHRIA','lenovo',30000,1467890223);
Query OK, 1 row affected (0.02 sec)

mysql> insert into product values(3500,'SHEELA','speaker',35000,1344523245);
Query OK, 1 row affected (0.01 sec)

mysql> insert into product values(4000,'LEELA','CPU',40000,1356873456);
Query OK, 1 row affected (0.01 sec)

mysql> insert into product values(4500,'ROSE','computer',45000,1378956884);
Query OK, 1 row affected (0.01 sec)

mysql> insert into product values(5000,'HARSH','speaker',50000,1567679044);
Query OK, 1 row affected (0.01 sec)

mysql> select * from product;
+------+--------+----------+-------+------------+
| SNO  | NAME   | PNAME    | PRICE | PNO        |
+------+--------+----------+-------+------------+
| 1000 | PRIYA  | lenovo   | 10000 | 1345678905 |
| 1500 | RIYA   | printer  | 15000 | 1335668817 |
| 2000 | LIRA   | lenovo   | 20000 | 1345678875 |
| 2500 | LUSIA  | printer  | 25000 | 1455677876 |
| 3000 | SHRIA  | lenovo   | 30000 | 1467890223 |
| 3500 | SHEELA | speaker  | 35000 | 1344523245 |
| 4000 | LEELA  | CPU      | 40000 | 1356873456 |
| 4500 | ROSE   | computer | 45000 | 1378956884 |
| 5000 | HARSH  | speaker  | 50000 | 1567679044 |
+------+--------+----------+-------+------------+
9 rows in set (0.00 sec)

mysql> select sum(PRICE) 'TOTAL' from product;
+--------+
| TOTAL  |
+--------+
| 270000 |
+--------+
1 row in set (0.00 sec)

mysql> select max(PRICE) 'MAXIMUM' from product;
+---------+
| MAXIMUM |
+---------+
|   50000 |
+---------+
1 row in set (0.00 sec)

mysql> select min(PRICE) 'MINIMUM' from product;
+---------+
| MINIMUM |
+---------+
|   10000 |
+---------+
1 row in set (0.00 sec)

mysql> select Avg(PRICE) 'AVERAGE' from product;
+------------+
| AVERAGE    |
+------------+
| 30000.0000 |
+------------+
1 row in set (0.00 sec)

mysql> select count(*) 'NO OF ORDERS' from product;
+--------------+
| NO OF ORDERS |
+--------------+
|            9 |
+--------------+
1 row in set (0.01 sec)

mysql> select * from product order by NAME asc
    -> select * from product order by NAME asc;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'select * from product order by NAME asc' at line 2
mysql> select * from product order by NAME asc;
+------+--------+----------+-------+------------+
| SNO  | NAME   | PNAME    | PRICE | PNO        |
+------+--------+----------+-------+------------+
| 5000 | HARSH  | speaker  | 50000 | 1567679044 |
| 4000 | LEELA  | CPU      | 40000 | 1356873456 |
| 2000 | LIRA   | lenovo   | 20000 | 1345678875 |
| 2500 | LUSIA  | printer  | 25000 | 1455677876 |
| 1000 | PRIYA  | lenovo   | 10000 | 1345678905 |
| 1500 | RIYA   | printer  | 15000 | 1335668817 |
| 4500 | ROSE   | computer | 45000 | 1378956884 |
| 3500 | SHEELA | speaker  | 35000 | 1344523245 |
| 3000 | SHRIA  | lenovo   | 30000 | 1467890223 |
+------+--------+----------+-------+------------+
9 rows in set (0.00 sec)

mysql> select * from product order by NAME desc;
+------+--------+----------+-------+------------+
| SNO  | NAME   | PNAME    | PRICE | PNO        |
+------+--------+----------+-------+------------+
| 3000 | SHRIA  | lenovo   | 30000 | 1467890223 |
| 3500 | SHEELA | speaker  | 35000 | 1344523245 |
| 4500 | ROSE   | computer | 45000 | 1378956884 |
| 1500 | RIYA   | printer  | 15000 | 1335668817 |
| 1000 | PRIYA  | lenovo   | 10000 | 1345678905 |
| 2500 | LUSIA  | printer  | 25000 | 1455677876 |
| 2000 | LIRA   | lenovo   | 20000 | 1345678875 |
| 4000 | LEELA  | CPU      | 40000 | 1356873456 |
| 5000 | HARSH  | speaker  | 50000 | 1567679044 |
+------+--------+----------+-------+------------+
9 rows in set (0.00 sec)

mysql> select count(SNO), PNAME from product group by PNAME order by count(PNAME) desc;
+------------+----------+
| count(SNO) | PNAME    |
+------------+----------+
|          3 | lenovo   |
|          2 | printer  |
|          2 | speaker  |
|          1 | CPU      |
|          1 | computer |
+------------+----------+
5 rows in set (0.00 sec)

mysql> create table student (ID int(25) primary key,NAME varchar (56), DEPARTMENT varchar (67), DATEOFJOIN varchar (123));
Query OK, 0 rows affected, 1 warning (0.05 sec)

mysql> desc student;
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| ID         | int          | NO   | PRI | NULL    |       |
| NAME       | varchar(56)  | YES  |     | NULL    |       |
| DEPARTMENT | varchar(67)  | YES  |     | NULL    |       |
| DATEOFJOIN | varchar(123) | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+
4 rows in set (0.01 sec)

mysql> insert into student values (1000,'PRIYA','BSC CHEMISTRY','12-02-22');
Query OK, 1 row affected (0.01 sec)

mysql> insert into student values (1500,'RIYA','BSC MATHS','13-03-22');
Query OK, 1 row affected (0.01 sec)

mysql> insert into student values (2000,'SHRIA','BSC PHYSICS','14-04-23');
Query OK, 1 row affected (0.01 sec)

mysql> insert into student values (2500,'SHEELA','BA ENGLISH','25-05-23');
Query OK, 1 row affected (0.01 sec)

mysql> select * from student;
+------+--------+---------------+------------+
| ID   | NAME   | DEPARTMENT    | DATEOFJOIN |
+------+--------+---------------+------------+
| 1000 | PRIYA  | BSC CHEMISTRY | 12-02-22   |
| 1500 | RIYA   | BSC MATHS     | 13-03-22   |
| 2000 | SHRIA  | BSC PHYSICS   | 14-04-23   |
| 2500 | SHEELA | BA ENGLISH    | 25-05-23   |
+------+--------+---------------+------------+
4 rows in set (0.00 sec)

mysql> alter table student add mobile_no int(25);
Query OK, 0 rows affected, 1 warning (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 1

mysql> select * from student;
+------+--------+---------------+------------+-----------+
| ID   | NAME   | DEPARTMENT    | DATEOFJOIN | mobile_no |
+------+--------+---------------+------------+-----------+
| 1000 | PRIYA  | BSC CHEMISTRY | 12-02-22   |      NULL |
| 1500 | RIYA   | BSC MATHS     | 13-03-22   |      NULL |
| 2000 | SHRIA  | BSC PHYSICS   | 14-04-23   |      NULL |
| 2500 | SHEELA | BA ENGLISH    | 25-05-23   |      NULL |
+------+--------+---------------+------------+-----------+
4 rows in set (0.00 sec)

mysql> alter table student modify MOBILE_NO int;
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from student ;
+------+--------+---------------+------------+-----------+
| ID   | NAME   | DEPARTMENT    | DATEOFJOIN | MOBILE_NO |
+------+--------+---------------+------------+-----------+
| 1000 | PRIYA  | BSC CHEMISTRY | 12-02-22   |      NULL |
| 1500 | RIYA   | BSC MATHS     | 13-03-22   |      NULL |
| 2000 | SHRIA  | BSC PHYSICS   | 14-04-23   |      NULL |
| 2500 | SHEELA | BA ENGLISH    | 25-05-23   |      NULL |
+------+--------+---------------+------------+-----------+
4 rows in set (0.00 sec)

mysql> alter table student rename column ID to SNO;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from student;
+------+--------+---------------+------------+-----------+
| SNO  | NAME   | DEPARTMENT    | DATEOFJOIN | MOBILE_NO |
+------+--------+---------------+------------+-----------+
| 1000 | PRIYA  | BSC CHEMISTRY | 12-02-22   |      NULL |
| 1500 | RIYA   | BSC MATHS     | 13-03-22   |      NULL |
| 2000 | SHRIA  | BSC PHYSICS   | 14-04-23   |      NULL |
| 2500 | SHEELA | BA ENGLISH    | 25-05-23   |      NULL |
+------+--------+---------------+------------+-----------+
4 rows in set (0.00 sec)

mysql> rename table student to STUDENT_DETAILS;
Query OK, 0 rows affected (0.04 sec)

mysql> select * from student;
ERROR 1146 (42S02): Table 'taskonmysql.student' doesn't exist
mysql> select * from STUDENT_DETAILS;
+------+--------+---------------+------------+-----------+
| SNO  | NAME   | DEPARTMENT    | DATEOFJOIN | MOBILE_NO |
+------+--------+---------------+------------+-----------+
| 1000 | PRIYA  | BSC CHEMISTRY | 12-02-22   |      NULL |
| 1500 | RIYA   | BSC MATHS     | 13-03-22   |      NULL |
| 2000 | SHRIA  | BSC PHYSICS   | 14-04-23   |      NULL |
| 2500 | SHEELA | BA ENGLISH    | 25-05-23   |      NULL |
+------+--------+---------------+------------+-----------+
4 rows in set (0.01 sec)

mysql> truncate table STUDENT_DETAILS;
Query OK, 0 rows affected (0.06 sec)

mysql> select * from STUDENT_DETAILS;
Empty set (0.01 sec)

mysql> drop table STUDENT_DETAILS;
Query OK, 0 rows affected (0.04 sec)

mysql> select * from STUDENT_DETAILS;
ERROR 1146 (42S02): Table 'taskonmysql.student_details' doesn't exist
mysql> create table students (ID int(25) primary key,NAME varchar (56), DEPARTMENT varchar (67), DATEOFJOIN varchar (123));
Query OK, 0 rows affected, 1 warning (0.06 sec)

mysql> desc students;
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| ID         | int          | NO   | PRI | NULL    |       |
| NAME       | varchar(56)  | YES  |     | NULL    |       |
| DEPARTMENT | varchar(67)  | YES  |     | NULL    |       |
| DATEOFJOIN | varchar(123) | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+
4 rows in set (0.01 sec)

mysql> insert into students values (1000,'PRIYA','BSC CHEMISTRY','12-02-22');
Query OK, 1 row affected (0.01 sec)

mysql> insert into students values (1500,'RIYA','BSC MATHS','13-03-22');
Query OK, 1 row affected (0.01 sec)

mysql> insert into students values (2000,'SHRIA','BSC PHYSICS','14-04-23');
Query OK, 1 row affected (0.01 sec)

mysql> insert into students values (2500,'SHEELA','BA ENGLISH','25-05-23');
Query OK, 1 row affected (0.01 sec)

mysql> select * from students;
+------+--------+---------------+------------+
| ID   | NAME   | DEPARTMENT    | DATEOFJOIN |
+------+--------+---------------+------------+
| 1000 | PRIYA  | BSC CHEMISTRY | 12-02-22   |
| 1500 | RIYA   | BSC MATHS     | 13-03-22   |
| 2000 | SHRIA  | BSC PHYSICS   | 14-04-23   |
| 2500 | SHEELA | BA ENGLISH    | 25-05-23   |
+------+--------+---------------+------------+
4 rows in set (0.00 sec)

mysql> update students set DEPARTMENT='BA HISTORY' where ID=2;
Query OK, 0 rows affected (0.01 sec)
Rows matched: 0  Changed: 0  Warnings: 0

mysql> select * from students;
+------+--------+---------------+------------+
| ID   | NAME   | DEPARTMENT    | DATEOFJOIN |
+------+--------+---------------+------------+
| 1000 | PRIYA  | BSC CHEMISTRY | 12-02-22   |
| 1500 | RIYA   | BSC MATHS     | 13-03-22   |
| 2000 | SHRIA  | BSC PHYSICS   | 14-04-23   |
| 2500 | SHEELA | BA ENGLISH    | 25-05-23   |
+------+--------+---------------+------------+
4 rows in set (0.00 sec)

mysql> UPDATE students set DEPARTMENT='BA HISTORY' where ID=2;
Query OK, 0 rows affected (0.00 sec)
Rows matched: 0  Changed: 0  Warnings: 0

mysql> select * from students;
+------+--------+---------------+------------+
| ID   | NAME   | DEPARTMENT    | DATEOFJOIN |
+------+--------+---------------+------------+
| 1000 | PRIYA  | BSC CHEMISTRY | 12-02-22   |
| 1500 | RIYA   | BSC MATHS     | 13-03-22   |
| 2000 | SHRIA  | BSC PHYSICS   | 14-04-23   |
| 2500 | SHEELA | BA ENGLISH    | 25-05-23   |
+------+--------+---------------+------------+
4 rows in set (0.00 sec)

mysql> update students set DEPARTMENT='BA HISTORY' where ID=1500;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from students;
+------+--------+---------------+------------+
| ID   | NAME   | DEPARTMENT    | DATEOFJOIN |
+------+--------+---------------+------------+
| 1000 | PRIYA  | BSC CHEMISTRY | 12-02-22   |
| 1500 | RIYA   | BA HISTORY    | 13-03-22   |
| 2000 | SHRIA  | BSC PHYSICS   | 14-04-23   |
| 2500 | SHEELA | BA ENGLISH    | 25-05-23   |
+------+--------+---------------+------------+
4 rows in set (0.00 sec)

mysql> delete from students where ID=2500;
Query OK, 1 row affected (0.02 sec)

mysql> select * from students;
+------+-------+---------------+------------+
| ID   | NAME  | DEPARTMENT    | DATEOFJOIN |
+------+-------+---------------+------------+
| 1000 | PRIYA | BSC CHEMISTRY | 12-02-22   |
| 1500 | RIYA  | BA HISTORY    | 13-03-22   |
| 2000 | SHRIA | BSC PHYSICS   | 14-04-23   |
+------+-------+---------------+------------+
3 rows in set (0.00 sec)

mysql> desc product;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| SNO   | int         | YES  |     | NULL    |       |
| NAME  | varchar(20) | YES  |     | NULL    |       |
| PNAME | varchar(28) | YES  |     | NULL    |       |
| PRICE | int         | YES  |     | NULL    |       |
| PNO   | varchar(29) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

mysql> select * from product;
+------+--------+----------+-------+------------+
| SNO  | NAME   | PNAME    | PRICE | PNO        |
+------+--------+----------+-------+------------+
| 1000 | PRIYA  | lenovo   | 10000 | 1345678905 |
| 1500 | RIYA   | printer  | 15000 | 1335668817 |
| 2000 | LIRA   | lenovo   | 20000 | 1345678875 |
| 2500 | LUSIA  | printer  | 25000 | 1455677876 |
| 3000 | SHRIA  | lenovo   | 30000 | 1467890223 |
| 3500 | SHEELA | speaker  | 35000 | 1344523245 |
| 4000 | LEELA  | CPU      | 40000 | 1356873456 |
| 4500 | ROSE   | computer | 45000 | 1378956884 |
| 5000 | HARSH  | speaker  | 50000 | 1567679044 |
+------+--------+----------+-------+------------+
9 rows in set (0.00 sec)

mysql> lock table product read;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from product;
+------+--------+----------+-------+------------+
| SNO  | NAME   | PNAME    | PRICE | PNO        |
+------+--------+----------+-------+------------+
| 1000 | PRIYA  | lenovo   | 10000 | 1345678905 |
| 1500 | RIYA   | printer  | 15000 | 1335668817 |
| 2000 | LIRA   | lenovo   | 20000 | 1345678875 |
| 2500 | LUSIA  | printer  | 25000 | 1455677876 |
| 3000 | SHRIA  | lenovo   | 30000 | 1467890223 |
| 3500 | SHEELA | speaker  | 35000 | 1344523245 |
| 4000 | LEELA  | CPU      | 40000 | 1356873456 |
| 4500 | ROSE   | computer | 45000 | 1378956884 |
| 5000 | HARSH  | speaker  | 50000 | 1567679044 |
+------+--------+----------+-------+------------+
9 rows in set (0.00 sec)

mysql> LOCk table product read;
Query OK, 0 rows affected (0.00 sec)

mysql> alter table product modify PNO int;
ERROR 1099 (HY000): Table 'product' was locked with a READ lock and can't be updated
mysql> LOCk table product write;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from product where SNO='1500' LOCK IN SHARE MODE;
+------+------+---------+-------+------------+
| SNO  | NAME | PNAME   | PRICE | PNO        |
+------+------+---------+-------+------------+
| 1500 | RIYA | printer | 15000 | 1335668817 |
+------+------+---------+-------+------------+
1 row in set (0.01 sec)

mysql> unlock tables;
Query OK, 0 rows affected (0.00 sec)

mysql> alter table product modify PNO int;
Query OK, 9 rows affected (0.09 sec)
Records: 9  Duplicates: 0  Warnings: 0
