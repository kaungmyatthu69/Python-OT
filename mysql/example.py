import mysql.connector
db_connecion=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nankhan",
    database="onlinedb"
)
x=0

data_list=[]
while x<2:
    id=1
    name=input("Please enter your name>>")
    age=input("Please enter your age>>")
    job=input("Please enter your job >>")
    hobby=input("Please enter your hobby>>")
    ID_Card=input ('Please enter your ID>>')
    print("Plz enter next one!!")
    id=x+1
    tu=(id,name,age,job,hobby,ID_Card)
    data_list.append(tu)
    
    x+=1
   
db_Cursor=db_connecion.cursor( )
#db_Cursor.execute("CREATE TABLE Online5(id int primary key AUTO_INCREMENT,name VARCHAR(30),age SMALLINT,job VARCHAR(30),hobby VARCHAR(30),ID_Card TINYINT)")
data_type="INSERT INTO Online5(id,name,age,job,hobby,ID_Card)values(%s,%s,%s,%s,%s,%s)"
data=data_list
db_Cursor.executemany(data_type,data)
db_connecion.commit()
print('data insert')
print(db_Cursor.rowcount)
db_Cursor.execute("SELECT * FROM Online3")
for d in db_Cursor:
    print(d)