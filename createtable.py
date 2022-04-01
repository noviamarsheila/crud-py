import mysql.connector

mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "novia"
)

myhandle = mydatabase.cursor()
myhandle.execute("CREATE TABLE datadiri (id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(200), umur CHAR(100), desa VARCHAR(255), kota VARCHAR(255) )")
