import mysql.connector
db_connecion=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nankhan",
    database="onlinedb"

)
db_Cursor=db_connecion.cursor()
#db_Cursor.execute("CREATE TABLE Online (id int primary key  AUTO_INCREMENT,namen VARCHAR(30),age SMALLINT,atttend TINYINT)")
db_Cursor.execute("DESCRIBE Online")
for db in db_Cursor:
    print(db)