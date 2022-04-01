import mysql.connector

mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "novia"
)

myhandle = mydatabase.cursor()

sql = "INSERT INTO datadiri (id, nama, umur, desa, kota) VALUES (%s, %s, %s, %s, %s)"
value = [
    ("", "Berlian", 12, "Lasem", "Rembang"),
    ("", "Rival", 14, "Pamotan", "Rembang"),
    ("", "Putra", 19, "Sendang agung", "Rembang"),
    ("", "Ida", 18, "Gunem", "Rembang"),
    ("", "Nindi", 18, "Lasem", "Rembang")
]

myhandle.executemany(sql, value)

mydatabase.commit()
print(myhandle.rowcount, " data ditambahkan")