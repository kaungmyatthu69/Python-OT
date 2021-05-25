import mysql.connector
db_connecion=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nankhan",
    database="onlinedb"
)
db_Cursor=db_connecion.cursor()
#db_Cursor.execute("CREATE TABLE Online2(id int primary key AUTO_INCREMENT,name VARCHAR(30),age SMALLINT,attend TINYINT)")
#db_Cursor.execute("ALTER TABLE Online2 ADD hobby VARCHAR(30)")
data_type="INSERT INTO Online2(id,name,age,attend,hobby)values(%s,%s,%s,%s,%s)"
data=[(101,"kaung myat thu",20,10,"reading"),
(102,"kaung myat",20,10,"reading"),
(103,"kaung thu",20,10,"reading"),
(104,"myat thu",20,10,"reading"),
(105,"myat thu kaung",20,10,"reading")]
#db_Cursor.executemany(data_type,data)
db_connecion.commit()
print("inserted data")

db_Cursor.execute("SELECT * FROM Online2")
for d in db_Cursor:
    print (d)
print(db_Cursor.rowcount)

