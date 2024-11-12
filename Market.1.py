# Inisialisasi database buah
database_buah = [
    {"nama": "Apel", "harga": 10000, "stok": 20},
    {"nama": "Jeruk", "harga": 15000, "stok": 15},
    {"nama": "Anggur", "harga": 20000, "stok": 25}
]

def menampilkan_daftar_buah(database_buah):
    """Menampilkan daftar buah yang tersedia."""
    if not database_buah:  # Cek apakah database kosong
        print("Database buah kosong.")
        return

    print("\nDaftar Buah:")
    print("-" * 60)
    print("Index \t | Nama \t\t | Stock \t | Harga")
    print("-" * 60)
    for i, buah in enumerate(database_buah):
        print(f"{i} \t | {buah['nama']} \t\t | {buah['stok']} \t\t | {buah['harga']}")

def menambah_buah(database_buah):
    """Menambahkan buah baru ke dalam database."""
    nama = input("Masukkan nama buah: ")
    while True:
        try:
            harga = int(input("Masukkan harga buah: "))
            if harga > 0:  # Validasi harga harus positif
                break
            else:
                print("Harga harus lebih dari 0.")
        except ValueError:
            print("Input harga harus berupa angka.")
    while True:
        try:
            stok = int(input("Masukkan stok buah: "))
            if stok > 0:  # Validasi stok harus positif
                break
            else:
                print("Stok harus lebih dari 0.")
        except ValueError:
            print("Input stok harus berupa angka.")
    database_buah.append({"nama": nama, "harga": harga, "stok": stok})
    print("Buah berhasil ditambahkan!")

def menghapus_buah(database_buah):
    """Menghapus buah dari database."""
    if not database_buah:  # Cek apakah database kosong
        print("Database buah kosong.")
        return

    menampilkan_daftar_buah(database_buah)
    while True:
        try:
            index = int(input("Masukkan index buah yang ingin dihapus: "))
            if 0 <= index < len(database_buah):
                del database_buah[index]
                print("Buah berhasil dihapus!")
                break
            else:
                print("Index tidak valid.")
        except ValueError:
            print("Input index harus berupa angka.")

def membeli_buah(database_buah):
    """Memproses pembelian buah."""
    if not database_buah:  # Cek apakah database kosong
        print("Database buah kosong.")
        return

    cart = []
    while True:
        menampilkan_daftar_buah(database_buah)
        while True:
            try:
                index = int(input("Masukkan index buah yang ingin dibeli: "))
                break
            except ValueError:
                print("Input index harus berupa angka.")
        while True:
            try:
                jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
                if jumlah > 0:  # Validasi jumlah harus positif
                    break
                else:
                    print("Jumlah harus lebih dari 0.")
            except ValueError:
                print("Input jumlah harus berupa angka.")

        if 0 <= index < len(database_buah):
            buah = database_buah[index]
            if jumlah <= buah['stok']:
                cart.append({"nama": buah['nama'], "qty": jumlah, "harga": buah['harga']})
                buah['stok'] -= jumlah
                print(f"{jumlah} {buah['nama']} berhasil ditambahkan ke keranjang.")
            else:
                print(f"Stock tidak cukup, stock {buah['nama']} tinggal {buah['stok']}")
        else:
            print("Index tidak valid.")

        lanjut = input("Mau beli yang lain? (ya/tidak): ")
        if lanjut.lower() != "ya":
            break

    # Menampilkan daftar belanja dan menghitung total harga
    if cart:
        print("\nDaftar Belanja:")
        print("Nama \t\t | Qty \t | Harga \t | Total Harga")
        print("-" * 60)
        total_harga = 0
        for item in cart:
            total_item = item['qty'] * item['harga']
            print(f"{item['nama']} \t\t | {item['qty']} \t | {item['harga']} \t | {total_item}")
            total_harga += total_item
        print(f"Total Yang Harus Dibayar = {total_harga}")

        # Memproses pembayaran
        while True:
            try:
                uang = int(input("Masukkan jumlah uang: "))
                if uang >= total_harga:
                    kembalian = uang - total_harga
                    print("Terima kasih")
                    print(f"Uang kembali anda: {kembalian}")
                    break
                else:
                    print("Uang anda kurang")
            except ValueError:
                print("Input uang harus berupa angka.")
    else:
        print("Anda tidak membeli apa-apa.")

# Loop utama program
while True:
    print("\nList Menu:")
    print("1. Menampilkan Daftar Buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit Program")

    pilihan = input("Masukkan angka Menu yang ingin dijalankan: ")

    if pilihan == "1":
        menampilkan_daftar_buah(database_buah)
    elif pilihan == "2":
        menambah_buah(database_buah)
    elif pilihan == "3":
        menghapus_buah(database_buah)
    elif pilihan == "4":
        membeli_buah(database_buah)
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")