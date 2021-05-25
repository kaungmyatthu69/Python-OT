import mysql.connector
dbconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nankhan"

)
print(dbconnection)