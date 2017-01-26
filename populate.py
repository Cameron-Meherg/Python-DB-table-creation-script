import sqlite3
import MySQLdb
import psycopg2
import json

def getData():
	faculty = json.load(open('faculty.json'))
	classes = json.load(open('class.json'))
	enroll = json.load(open('Enroll.json'))
	student = json.load(open('student.json'))
	return {'faculty':faculty, 'class':classes,'enroll':enroll,'student':student}
def insertRow(row,conn1,conn2,conn3):
	conn1.execute(row)
	conn2.execute(row)
	conn3.execute(row)

tables = getData()

facultyInsert = "INSERT INTO Faculty VALUES('{}','{}','{}','{}');"
classInsert = "INSERT INTO Class VALUES('{}','{}','{}','{}');"
enrollInsert = "INSERT INTO Enroll VALUES('{}','{}','{}');"
studentInsert = "INSERT INTO Student VALUES('{}','{}','{}','{}','{}');"

litConn = sqlite3.connect('university.sqlite')
litCursor = litConn.cursor()

mysqlConn = MySQLdb.connect('localhost','testuser','test123','university')
mysqlCurr = mysqlConn.cursor()

postConn = psycopg2.connect("dbname='university' user='postgres' host='localhost' password='test123'")
postCurr = postConn.cursor()


	
for row in tables['faculty']:
	tmp = facultyInsert.format(row['facId'],row['name'],row['department'],row['rank'])
	print(tmp)
	insertRow(tmp,litCursor,mysqlCurr,postCurr)
	litConn.commit()
	mysqlConn.commit()
	postConn.commit()

for row in tables['class']:
	tmp = classInsert.format(row['classNumber'],row['facId'],row['schedule'],row['room'])
	print(tmp)
	insertRow(tmp,litCursor,mysqlCurr,postCurr)
	litConn.commit()
	mysqlConn.commit()
	postConn.commit()

for row in tables['enroll']:
	tmp = enrollInsert.format(row['stuId'],row['classNumber'],row['grade'])
	print(tmp)
	insertRow(tmp,litCursor,mysqlCurr,postCurr)
	litConn.commit()
	mysqlConn.commit()
	postConn.commit()

for row in tables['student']:
	tmp = studentInsert.format(row['stuId'],row['lastName'],row['firstName'],row['major'],row['credits'])
	print(tmp)
	insertRow(tmp,litCursor,mysqlCurr,postCurr)
	litConn.commit()
	mysqlConn.commit()
	postConn.commit()

postConn.close()
mysqlConn.close()
litConn.close()