import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="",
    database = "latihandb"
)

mycursor = mydb.cursor()

print("1. Data")
print("2. Input Data")
print("3. Hapus")

def tampil():
    mycursor.execute("SELECT * FROM biodata")
    result = mycursor.fetchall()
    for i in result:
        print(i)

def tambah():
    print("Masukkan data")
    nama =  str(input("Nama : "))
    umur = int(input("Umur : "))
    sql = "INSERT INTO biodata (id,nama, umur) VALUES (%s,%s,%s)"
    val = ("",nama, umur)
    mycursor.execute(sql, val)
    mydb.commit()

def hapus():
    tampil()
    s = str(input("masukkan id : "))
    mycursor.execute("DELETE FROM biodata WHERE id = " + s  )
    mydb.commit()


pil = int(input("masukkan pilihan : "))

if pil == 1:
    tampil()
elif pil == 2:
    tambah()
elif pil == 3:
    hapus()
else:
    print("-")