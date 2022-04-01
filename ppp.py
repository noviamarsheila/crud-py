def menu():
    print("======================================================")
    print("                 DAFTAR GAJI KARYAWAN                 ")
    print("======================================================")
    print("KODE             Posisi          gaji           pajak ")
    print("------------------------------------------------------")
    print("DSNX             Dosen        3.000.000          5%   ")
    print("STPM             Satpam       2.000.000          3%   ")
    print("OFFC             Officer      2.800.000         2.5%  ")
    print("CSOF             CS office    2.500.000          3%   ")
    print("------------------------------------------------------")


menu()

status = input("Apakah anda karyawan disini ? Y/N --> ")

gajiDosen = 3000000
gajiSatpam = 2000000
gajiOfficer = 2800000
gajiCsoffice = 2500000
pajakDosen = 0.05
pajakSatpam = 0.03
pajakOfficer = 0.025
pajakCsoffice = 0.03
users = []


if status == "Y":
    jumlahInput = int(input("Ingin memakai aplikasi berapa kali : "))

    i = 0
    while i < jumlahInput:
        print("Perhitungan ke - ", i+1)
        nama = input("Masukkan nama anda : ")
        users.append(nama)

        if status == "Y":
            print(nama, " termasuk karyawan disini")
            jabatan = input("masukkan kode jabatan anda ")
            if jabatan == "DSNX":
                totalGaji = gajiDosen - (gajiDosen*pajakDosen)
                print("Gaji yang anda dapatkan bulan ini Rp ", totalGaji)
            elif jabatan == "STPM":
                totalGaji = gajiSatpam - (gajiSatpam*pajakSatpam)
                print("Gaji yang anda dapatkan bulan ini Rp ", totalGaji)
            elif jabatan == "OFFC":
                totalGaji = gajiOfficer - (gajiOfficer*pajakOfficer)
                print("Gaji yang anda dapatkan bulan ini Rp ", totalGaji)
            elif jabatan == "CSOF":
                totalGaji = gajiCsoffice - (gajiCsoffice*pajakCsoffice)
                print("Gaji yang anda dapatkan bulan ini Rp ", totalGaji)
            else:
                print("pilihan anda tidak ditemukan")

        else:
            print("Sistem ini hanya untuk karyawan")

        i += 1

    def garis():
        print("====================================================")

    garis()
    print("           Riwayat pemakaian aplikasi               ")
    garis()
    print(users)


elif status == "N":
    print("Aplikasi ini khusus karyawan saja")
