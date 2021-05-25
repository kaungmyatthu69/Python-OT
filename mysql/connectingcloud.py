import mysql.connector
db_connection=mysql.connector.connect(
    host="bspxc5tdqp77kw4pdgqo-mysql.services.clever-cloud.com",
    user="u4vfynlu7qzzjloi",
    passwd="4YJrkCdQyjtoTaCt95Up",
    database="bspxc5tdqp77kw4pdgqo"
)
db_Cursor=db_connection.cursor()
#db_Cursor.execute("SHOW databases")
db_Cursor.execute("CREATE TABLE cloudDB (id int,name VARCHAR(30),age SMALLINT)")
db_Cursor.execute("DESCRIBE cloudDB")
for db in db_Cursor:
    print(db)