import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='hoilamgi',
    database='ledongdb'
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)



