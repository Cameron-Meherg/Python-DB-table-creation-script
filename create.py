import sqlite3
import MySQLdb
import psycopg2

#CREATE TABLE table_name(  column1 datatype, PRIMARY KEY( one or more columns ));
Student = "CREATE TABLE IF NOT EXISTS Student(stuId varchar(15),lastName varchar(15),firstName varchar(15),major varchar(15), credits int, PRIMARY KEY(stuId));"
Faculty = "CREATE TABLE IF NOT EXISTS Faculty(facId varchar(15),name varchar(15),department varchar(15),rank varchar(15), PRIMARY KEY(facId));"
Class = "CREATE TABLE IF NOT EXISTS Class(classNumber varchar(15),facId varchar(15),schedule varchar(15),room varchar(15), PRIMARY KEY(classNumber));"
Enroll = "CREATE TABLE IF NOT EXISTS Enroll(stuId varchar(15),classNumber varchar(15),grade varchar(5),PRIMARY KEY(stuId,classNumber));"

tables = [Student,Faculty,Class,Enroll]
litConn = sqlite3.connect('IT350.sqlite')
litCursor = litConn.cursor()

mysqlConn = MySQLdb.connect('localhost','testuser','test123','IT350')
mysqlCurr = mysqlConn.cursor()

postConn = psycopg2.connect("dbname='it350' user='postgres' host='localhost' password='test123'")
postCurr = postConn.cursor()
for table in tables:
	print table
	#create the table on the sqlite
	litCursor.execute(table)

	#create the table on mysqldb
	mysqlCurr.execute(table)

	#create the table on postgress
	postCurr.execute(table)
postConn.close()
mysqlConn.close()
litConn.close()