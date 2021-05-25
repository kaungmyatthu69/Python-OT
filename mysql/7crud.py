import mysql.connector
db_connecion=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nankhan",
    database="Onlinedb"
)
db_Cursor=db_connecion.cursor()
#db_Cursor.execute("UPDATE online2 SET name ='Nan Khan' WHERE  id=102")
#db_Cursor.execute("DELETE FROM online2 WHERE id=102")
db_connecion.commit()
db_Cursor.execute("SELECT id,name,age FROM online2 ")
db=db_Cursor.fetchall()
for db in db:
    print(db)
