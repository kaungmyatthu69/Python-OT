import mysql.connector
dbconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nankhan"
)
dbCursor=dbconnection.cursor()
dbCursor.execute("CREATE DATABASE  myfirstdatabase")
dbCursor.execute("SHOW DATABASES")
for db in dbCursor:
    print(db)