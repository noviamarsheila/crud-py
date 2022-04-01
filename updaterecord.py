import mysql.connector

mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "novia"
)

myhandle = mydatabase.cursor()

sql = "UPDATE datadiri SET nama='Putri' WHERE nama='Nindi' "

myhandle.execute(sql)

mydatabase.commit()
print(myhandle.rowcount, " data diubah")