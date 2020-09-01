##import sqlite3
##
##conn = sqlite3.connect('students.db')
##c = conn.cursor()
##c.execute('''CREATE TABLE STUDENT(
##          ID INT PRIMARY KEY     NOT NULL,
##          NAME           TEXT    NOT NULL,
##          AGE            INT     NOT NULL,
##          ADDRESS        CHAR(50)
##          )''')
##conn.commit()
##conn.close()

##import sqlite3
##
##conn = sqlite3.connect('students.db')
##c = conn.cursor()
##c.execute('''INSERT INTO STUDENT
##             (ID,NAME,AGE,ADDRESS) 
##             VALUES (1, '刘晓华', 18, '北京市海淀区')
##          ''')
##c.execute('''INSERT INTO STUDENT
##              (ID,NAME,AGE,ADDRESS) 
##             VALUES (2, '张毅', 19, '北京市朝阳区')
##          ''')
##conn.commit()
##conn.close()


##import sqlite3
##
##conn = sqlite3.connect('students.db')
##c = conn.cursor()
##c.execute('SELECT * FROM STUDENT')
##print(c.fetchall())
###conn.commit()
##conn.close()

##import sqlite3

##conn = sqlite3.connect('students.db')
##c = conn.cursor()
##c.execute('UPDATE STUDENT SET AGE = 17 WHERE ID=2')
##conn.commit()
##c.execute('SELECT * FROM STUDENT')
##print(c.fetchall())
##conn.close()


import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()
c.execute('DELETE FROM STUDENT WHERE AGE=17')
conn.commit()
c.execute('SELECT * FROM STUDENT')
print(c.fetchall())
conn.close()


