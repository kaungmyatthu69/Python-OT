import mysql.connector
db_connecion=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nankhan",
    database="onlinedb"
)
db_Cursor=db_connecion.cursor()
#db_Cursor.execute("SELECT id,name,age FROM online2 WHERE name LIKE 'k%'")indexing with k
#db_Cursor.execute("SELECT id,name,age FROM online2 WHERE id IN(100,101)")indexing with id number
db_Cursor.execute("SELECT id,name,age FROM online2 ORDER BY name")#by order arrange name
data=db_Cursor.fetchall()
for db in data:
    print("%d %s %d"%(db[0],db[1],db[2]))
