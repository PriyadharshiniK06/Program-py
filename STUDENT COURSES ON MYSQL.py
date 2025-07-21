(c) Microsoft Corporation. All rights reserved.

C:\Users\kumaran>mysql -u root -p
Enter password: ****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.37 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database collegecourse
    -> create database collegecourse;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'create database collegecourse' at line 2
mysql> create database collegecourse;
Query OK, 1 row affected (0.03 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| collegecourse      |
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
10 rows in set (0.05 sec)

mysql> use database collegecourse;
ERROR 1049 (42000): Unknown database 'database'
mysql> use collegecourse;
Database changed
mysql> create table studentdetails(NAME varchar(450),12TH_GROUP varchar(780),12TH_MARK int(10));
Query OK, 0 rows affected, 1 warning (0.06 sec)

mysql> insert into studentdetails values(PRIYA,COMPUTER_SCIENCE,500);
ERROR 1054 (42S22): Unknown column 'PRIYA' in 'field list'
mysql> insert into studentdetails values('PRIYA','COMPUTER SCIENCE',500);
Query OK, 1 row affected (0.02 sec)

mysql> insert into studentdetails values('HARSHINI','BIOLOGY',500);
Query OK, 1 row affected (0.01 sec)

mysql> insert into studentdetails values('VARINKA','COMMERCE',505);
Query OK, 1 row affected (0.02 sec)

mysql> insert into studentdetails values('RAJI','COMPUTER SCIENCE',510);
Query OK, 1 row affected (0.01 sec)

mysql> select * from student details;
ERROR 1146 (42S02): Table 'collegecourse.student' doesn't exist
mysql> select * from studentdetails;
+----------+------------------+-----------+
| NAME     | 12TH_GROUP       | 12TH_MARK |
+----------+------------------+-----------+
| PRIYA    | COMPUTER SCIENCE |       500 |
| HARSHINI | BIOLOGY          |       500 |
| VARINKA  | COMMERCE         |       505 |
| RAJI     | COMPUTER SCIENCE |       510 |
+----------+------------------+-----------+
4 rows in set (0.01 sec)

mysql> create table coursedetails (COURSE_NAME varchar(670), FEES-STRUCTURE varchar(560), PER_SEMESTER-FEES int(350));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '-STRUCTURE varchar(560), PER_SEMESTER-FEES int(350))' at line 1
mysql> create table coursedetails (COURSE_NAME varchar(670), FEES_STRUCTURE varchar(560), PER_SEMESTER_FEES int(350));
ERROR 1439 (42000): Display width out of range for column 'PER_SEMESTER_FEES' (max = 255)
mysql> create table coursedetails (COURSE_NAME varchar(670), FEES_STRUCTURE varchar(560), PER_SEMESTER_FEES int(240));
Query OK, 0 rows affected, 1 warning (0.06 sec)

mysql> insert into coursedetails values( 'B.TECH COMPUTER SCIENCE', '5 LAKHS FOR MANAGEMENT',999890);
Query OK, 1 row affected (0.02 sec)

mysql> insert into coursedetails values( 'B.TECH COMPUTER SCIENCE', '3.5 LAKHS FOR CENTAC',85890);
Query OK, 1 row affected (0.01 sec)

mysql> insert into coursedetails values( 'B.TECH EEE', '4.5 LAKHS FOR MANAGEMENT',99870);
Query OK, 1 row affected (0.01 sec)

mysql> insert into coursedetails values( 'B.TECH EEE', '4 LAKHS FOR CENTAC',85840);
Query OK, 1 row affected (0.01 sec)

mysql> insert into coursedetails values( 'B.TECH ECE', '5 LAKHS FOR MANAGEMENT',99890);
Query OK, 1 row affected (0.01 sec)

mysql> insert into coursedetails values( 'B.TECH ECE', '4 LAKHS FOR CENTAC',98890);
Query OK, 1 row affected (0.01 sec)

mysql> insert into coursedetails values( 'B.TECH AIML', '4.5 LAKHS FOR MANAGEMENT',97870);
Query OK, 1 row affected (0.01 sec)

mysql> insert into coursedetails values( 'B.TECH AIML', '4 LAKHS FOR CENTAC',95890);
Query OK, 1 row affected (0.01 sec)

mysql> create table biocourses (COURSE_NAME varchar(670), FEES_STRUCTURE varchar(560), PER_SEMESTER_FEES int(240));
Query OK, 0 rows affected, 1 warning (0.05 sec)

mysql> insert into biocourses values ('B.PHARM','5.5 LAKHS FOR MANAGEMENT',99980);
Query OK, 1 row affected (0.02 sec)

mysql> insert into biocourses values ('B.PHARM','5 LAKHS FOR CENTAC',99900);
Query OK, 1 row affected (0.01 sec)

mysql> insert into biocourses values ('B.SC COMPUTER SCIENCE','4 LAKHS FOR MANAGEMENT',67000);
Query OK, 1 row affected (0.01 sec)

mysql> insert into biocourses values ('B.SC CHEMISTRY','4 LAKHS FOR MANAGEMENT',67000);
Query OK, 1 row affected (0.01 sec)

mysql> insert into biocourses values ('B.SC PHYSICS','4 LAKHS FOR MANAGEMENT',67000);
Query OK, 1 row affected (0.01 sec)

mysql> insert into biocourses values ('B.SC MATHS','4 LAKHS FOR MANAGEMENT',67000);
Query OK, 1 row affected (0.01 sec)

mysql> insert into biocourses values ('B.A ENGLISH','3 LAKHS FOR MANAGEMENT',60000);
Query OK, 1 row affected (0.02 sec)

mysql> insert into biocourses values ('B.A HISTORY','3 LAKHS FOR MANAGEMENT',60000);
Query OK, 1 row affected (0.01 sec)

mysql> select * from coursedetails;
+-------------------------+--------------------------+-------------------+
| COURSE_NAME             | FEES_STRUCTURE           | PER_SEMESTER_FEES |
+-------------------------+--------------------------+-------------------+
| B.TECH COMPUTER SCIENCE | 5 LAKHS FOR MANAGEMENT   |            999890 |
| B.TECH COMPUTER SCIENCE | 3.5 LAKHS FOR CENTAC     |             85890 |
| B.TECH EEE              | 4.5 LAKHS FOR MANAGEMENT |             99870 |
| B.TECH EEE              | 4 LAKHS FOR CENTAC       |             85840 |
| B.TECH ECE              | 5 LAKHS FOR MANAGEMENT   |             99890 |
| B.TECH ECE              | 4 LAKHS FOR CENTAC       |             98890 |
| B.TECH AIML             | 4.5 LAKHS FOR MANAGEMENT |             97870 |
| B.TECH AIML             | 4 LAKHS FOR CENTAC       |             95890 |
+-------------------------+--------------------------+-------------------+
8 rows in set (0.00 sec)

mysql> select * from biocourses;
+-----------------------+--------------------------+-------------------+
| COURSE_NAME           | FEES_STRUCTURE           | PER_SEMESTER_FEES |
+-----------------------+--------------------------+-------------------+
| B.PHARM               | 5.5 LAKHS FOR MANAGEMENT |             99980 |
| B.PHARM               | 5 LAKHS FOR CENTAC       |             99900 |
| B.SC COMPUTER SCIENCE | 4 LAKHS FOR MANAGEMENT   |             67000 |
| B.SC CHEMISTRY        | 4 LAKHS FOR MANAGEMENT   |             67000 |
| B.SC PHYSICS          | 4 LAKHS FOR MANAGEMENT   |             67000 |
| B.SC MATHS            | 4 LAKHS FOR MANAGEMENT   |             67000 |
| B.A ENGLISH           | 3 LAKHS FOR MANAGEMENT   |             60000 |
| B.A HISTORY           | 3 LAKHS FOR MANAGEMENT   |             60000 |
+-----------------------+--------------------------+-------------------+
8 rows in set (0.00 sec)
