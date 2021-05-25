import mysql.connector
db_connecion=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nankhan",
    database="onlinedb"

)
db_Cursor=db_connecion.cursor()
#db_Cursor.execute("CREATE TABLE Online (id int primary key  AUTO_INCREMENT,namen VARCHAR(30),age SMALLINT,atttend TINYINT)")
#db_Cursor.execute("ALTER TABLE Online ADD hobby VARCHAR(30)")
dataType="INSERT INTO Online(id,namen,age,atttend,hobby)values(%s,%s,%s,%s,%s)"
data=(100,"Kaung Myat Thu",20,10,"ML Enginner")
#db_Cursor.execute(dataType ,data)# data insert code
db_connecion.commit()

print("inserted data")

db_Cursor.execute("SELECT * FROM Online")
for d in db_Cursor:
    print(d)
print(db_Cursor.rowcount)
