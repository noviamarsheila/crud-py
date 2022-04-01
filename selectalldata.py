import mysql.connector

mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "novia"
)

myhandle = mydatabase.cursor()
myhandle.execute("SELECT * FROM datadiri")

result = myhandle.fetchall()
for i in result:
    print(i)
