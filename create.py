import sqlite3
import MySQLdb
import psycopg2
litConn = sqlite3.connect('IT350.sqlite')
litCursor = litConn.cursor()

mysqlConn = MySQLdb.connect('localhost','testuser','test123','IT350')
mysqlCurr = mysqlConn.cursor()

postConn = psycopg2.connect("dbname='it350' user='postgres' host='localhost' password='test123'")
postCurr = postConn.cursor()

postConn.close()
mysqlConn.close()
litConn.close()