# Manajemen Keuangan 
# - Pencatatan Income # - Tampilkan Riwayat Transaksi # - Hitung Saldo Akhir


def keterangan():
    print("---------------------------------------------")
    print("| A. Pencatatan Income Dan Outcome          |")
    print("| B. Tampilkan Riwayat Transaksi            |")
    print("| C. Hitung Saldo Akhir                     |")
    print("| D. Keluar                                 |")
    print("---------------------------------------------")

income  = []
outcome = []

while True :
    keterangan()
    pilihan = input("Masukkan Pilihan Anda : ").upper()
    if pilihan == "A":
        pemasukkan  = float(input("Masukkan Pendapatan  : Rp "))
        pengeluaran = float(input("Masukkan Pengeluaran : Rp "))
        income.append(pemasukkan)
        outcome.append(pengeluaran)
        print(" Pemasukkan Dan Pengeluaran Telah Ditambahkan ").center(45, '+')
        print("-"*45)

    elif pilihan == "B":
        print("---------------------------------------------")
        print(" Riwayat Transaksi ".center(45,"="))
        print("| Pemasukkan  : Rp",sum(income))
        print("| Pengeluaran : Rp",sum(outcome))
        print("---------------------------------------------\n")

    elif pilihan == "C":
        saldo = sum(income) - sum(outcome)
        print("---------------------------------------------")
        print("| Total Pemasukan   : Rp",sum(income))
        print("| Total Pengeluaran : Rp",sum(outcome))
        print("| Total Saldo       : Rp",saldo)
        print("---------------------------------------------")

        if saldo >= 1:
            print(" Sediki Lagi Somo Kaya ".center(45, '+'))
            print("---------------------------------------------\n")

        elif saldo == 0 :
            print(" Kasian T Ada Perubahan ".center(45, '+'))
            print("---------------------------------------------\n")

        else :
            print(" Kase Banya Jo Itu Utang ".center(45, '+'))
            print("--------------------------------------------\n")

    elif pilihan == "D":
        print("-"*45)
        print("Terimakasih Atas Kepercayaan Kepada Kami".center(45,' '))
        print("Semoga Kelak Anda Jadi Orang Kaya".center(45,' '))
        print("AMIN".center(45,' '))
        print("-"*45)
        exit()

    else:
        print ("Mohon Masukkan Inputan Yang Sesuai")