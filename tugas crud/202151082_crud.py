# IMPORT KONEKTOR
import mysql.connector

# koneksi ke database
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database ="novia"
)

# SET CURSOR
myhandle = mydatabase.cursor()

# PILIHAN MENU
def menu():
    print("======================================================")
    print("                PILIHAN MENU APLIKASI                 ")
    print("======================================================")
    print("No             Aksi                                   ")
    print("------------------------------------------------------")
    print("1.             Tampilkan Data                         ")
    print("2.             Insert Data                            ")
    print("3.             Delete Data                            ")
    print("4.             Update Data                            ")
    print("5.             Cari Data                              ")
    print("6.             Keluar dari Aplikasi                   ")
    print("------------------------------------------------------")

menu()

# ------------------------------------FUNCTION ---------------------------------------------------
def tampilData():
    myhandle.execute("SELECT * FROM datadiri")
    result = myhandle.fetchall()
    for i in result:
        print(i)

def tambahData():
    print("Silahkan masukkan data dibawah ini ")
    nama =  str(input("Nama : "))
    umur = int(input("Umur : "))
    desa = str(input("Desa : "))
    kota = str(input("Kota : "))
    sql = "INSERT INTO datadiri (id, nama, umur, desa, kota) VALUES (%s,%s,%s,%s,%s)"
    value = ("",nama, umur, desa, kota)
    myhandle.execute(sql, value)
    mydatabase.commit()
    print(myhandle.rowcount, " data berhasil ditambahkan")

def hapusData():
    tampilData()
    idd = str(input("masukkan id data yang ingin anda hapus : "))
    myhandle.execute("DELETE FROM datadiri WHERE id = " + idd  )
    mydatabase.commit()
    print(myhandle.rowcount, " data berhasil dihapus")

def updateData():
    tampilData()
    idd = str(input("masukkan id data yang ingin anda ubah datanya  : "))
    nama = str(input("Nama : "))
    umur = int(input("Umur : "))
    desa = str(input("Desa : "))
    kota = str(input("Kota : "))
    sql = "UPDATE datadiri SET id = %s, nama = %s, umur = %s, desa = %s, kota = %s WHERE id= " + idd
    value = ("", nama, umur, desa, kota)
    myhandle.execute(sql, value)
    mydatabase.commit()
    print(myhandle.rowcount, " data diubah")

def cariData():
    keyword = input("Masukkan kata kunci pencarian : ")
    sql = "SELECT * FROM datadiri WHERE id LIKE %s OR nama LIKE %s OR umur LIKE %s OR desa LIKE %s OR kota LIKE %s"
    value = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword))
    myhandle.execute(sql, value)
    result = myhandle.fetchall()    
    if myhandle.rowcount < 0:
        print("Tidak ada data")
    else:
        for x in result:
            print(x)

# ------------------------------------END  FUNCTION ---------------------------------------------------

pilihan = int(input("masukkan pilihan : "))

if pilihan == 1:
    tampilData()
elif pilihan == 2:
    tambahData()
elif pilihan == 3:
    hapusData()
elif pilihan == 4:
    updateData()
elif pilihan == 5:
    cariData()
elif pilihan == 6:
    exit()
