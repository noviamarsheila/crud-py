import mysql.connector

mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "novia"
)

myhandle = mydatabase.cursor()

sql = "INSERT INTO datadiri (id, nama, umur, desa, kota) VALUES (%s, %s, %s, %s, %s)"
value = ("", "Sheila", 18, "Jeruk", "Rembang")

myhandle.execute(sql, value)

mydatabase.commit()
print(myhandle.rowcount, " data ditambahkan")