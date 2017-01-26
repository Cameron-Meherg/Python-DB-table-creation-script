import sqlite3
import MySQLdb
import psycopg2


dropFaculty = "DROP TABLE Faculty;"
dropEnroll = "DROP TABLE Enroll;"
dropClass = "DROP TABLE Class;"
dropStudent = "DROP TABLE Student;"

toDrop = [dropFaculty,dropEnroll,dropClass,dropStudent]
litConn = sqlite3.connect('university.sqlite')
litCursor = litConn.cursor()

mysqlConn = MySQLdb.connect('localhost','testuser','test123','university')
mysqlCurr = mysqlConn.cursor()

postConn = psycopg2.connect("dbname='university' user='postgres' host='localhost' password='test123'")
postCurr = postConn.cursor()

for each in toDrop:
	litCursor.execute(each)
	mysqlCurr.execute(each)
	postCurr.execute(each)
	litConn.commit()
	mysqlConn.commit()
	postConn.commit()

postConn.close()
mysqlConn.close()
litConn.close()