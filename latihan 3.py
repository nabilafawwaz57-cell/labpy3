saldo = 1000000

while True:
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    menu = input("Pilih menu (1/2): ")

    if menu == "1":
        tarik = int(input("Masukkan jumlah penarikan: "))
        if tarik > saldo:
            print("Saldo tidak cukup!")
        else:
            saldo -= tarik
            print("Penarikan berhasil!")
            if saldo == 0:
                print("Saldo Anda sudah habis!")
                break
    elif menu == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Menu tidak valid, silakan pilih 1 atau 2.")
