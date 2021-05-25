import mysql.connector
db_connecion=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='nankhan'
)
db_Cursor=db_connecion.cursor()
db_Cursor.execute("CREATE DATABASE onlinedb")
db_Cursor.execute("SHOW DATABASES")
for db in db_Cursor:
    print(db)