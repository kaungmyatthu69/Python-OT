import mysql.connector
db_connecion=mysql.connector.connect(
    host="bspxc5tdqp77kw4pdgqo-mysql.services.clever-cloud.com",
    user="u4vfynlu7qzzjloi",
    passwd="4YJrkCdQyjtoTaCt95Up",
    database="bspxc5tdqp77kw4pdgqo"
)
db_Cursor=db_connecion.cursor()
#db_Cursor.execute("CREATE TABLE online6(id int primary key AUTO_INCREMENT,monthly int,totalCost int)")
#dataType="INSERT INTO online6(id,monthly,totalCost)values(%s,%s,%s)"
#data=[(101,100,1000),(103,200,2400),(104,400,6000),(105,500,50000)]
#db_Cursor.executemany(dataType,data)
#db_connecion.commit()
db_Cursor.execute("SELECT online2.id,online2.name,online2.age,online6.id,online6.monthly,online6.totalCost FROM online6 join online2 on online6.id=online2.id ")
data=db_Cursor.fetchall()
for db in data:
    print("%d %s %d %d %d %d"%(db[0],db[1],db[2],db[3],db[4],db[5]))
    