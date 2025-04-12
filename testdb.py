import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="newdb")
#print(mydb)
cursor=conn.cursor()
cursor.execute("Select * from DataRevature.student")
for row in cursor:
    print(row)