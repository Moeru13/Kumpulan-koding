# Manajemen Keuangan 
# - Pencatatan Income # - Tampilkan Riwayat Transaksi # - Hitung Saldo Akhir

def keterangan():
    print("---------------------------------------------")
    print("| 1. Pencatatan Pemasukkan Dan Pengeluaran  |")
    print("| 2. Tampilkan Riwayat Transaksi            |")
    print("| 3. Hitung Saldo Akhir                     |")
    print("| 4. Keluar                                 |")
    print("---------------------------------------------")

def selesai():
    print("-"*45)
    print("Terimakasih Atas Kepercayaan Kepada Kami".center(45,' '))
    print("Semoga Kelak Anda Jadi Orang Kaya".center(45,' '))
    print("AMIN".center(45,' '))
    print("-"*45)
    exit()

income  = []
outcome = []

while True :
    # Menampilkan Menu
    keterangan()
    pilihan = input("Masukkan Pilihan Anda : ")

    # - Pencatatan Keuangan
    if pilihan == "1":
        pemasukkan  = float(input("Masukkan Pendapatan  : Rp "))
        pengeluaran = float(input("Masukkan Pengeluaran : Rp "))
        income.append(pemasukkan)
        outcome.append(pengeluaran)
        print()

    elif pilihan == "B":
        print("---------------------------------------------")
        print(" Riwayat Transaksi ".center(45,"="))
        print("| Pemasukkan  : Rp",sum(income))
        print("| Pengeluaran : Rp",sum(outcome))
        print("---------------------------------------------\n")

    elif pilihan == "C":
        saldo = sum(income) - sum(outcome)
        print(" Total Saldo ".center(45, "="))
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

        tanya = input("Tekan y untuk masuk ke menu utama : ").lower()
        if tanya == "y":
            print()
            continue
        else : 
            selesai()

    elif pilihan == "4":
        selesai()

    else:
        print ("Mohon Masukkan Inputan Yang Sesuai")