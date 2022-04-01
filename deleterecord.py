import mysql.connector

mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "novia"
)

myhandle = mydatabase.cursor()

sql = "DELETE FROM datadiri WHERE id=4"

myhandle.execute(sql)

mydatabase.commit()
print(myhandle.rowcount, " data dihapus")