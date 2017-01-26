import os

os.system("mysqldump -u testuser -ptest123 -h localhost university > mysql.sql")
os.system("pg_dump -h 127.0.0.1 -U testuser  university > postgres.sql")
os.system("sqlite3 university.sqlite .dump > sqlite.sql")