

# Inisialisasi data karyawan
data_karyawan = [
    {
        "id": "001",
        "nama": "Joni",
        "usia": 30,
        "jabatan": "Manager",
        "gaji": 10000000
    },
    {
        "id": "002",
        "nama": "Samsul",
        "usia": 25,
        "jabatan": "Staff",
        "gaji": 5000000
    },
    {
        "id": "003",
        "nama": "Wong FeHung",
        "usia": 28,
        "jabatan": "Supervisor",
        "gaji": 7000000
    }
]
def tampilkan_menu_utama(): #EROR HANDLING OK
    """Menampilkan menu utama program."""
    print("\nMenu Utama:")
    print("1. Tampilkan Data Karyawan")
    print("2. Tambah Data Karyawan")
    print("3. Ubah Data Karyawan")
    print("4. Hapus Data Karyawan")
    print("5. Keluar")

def tampilkan_menu_tampilkan_data():
    """Menampilkan menu untuk menampilkan data."""
    print("\nTampilkan Data:")
    print("1. Tampilkan Semua Data")
    print("2. Cari Data Karyawan")
    print("3. Kembali ke Menu Utama")

def tampilkan_menu_tambah_data():
    """Menampilkan menu untuk menambah data."""
    print("\nTambah Data:")
    print("1. Tambah Data Karyawan")
    print("2. Kembali ke Menu Utama")

def tampilkan_menu_ubah_data():
    """Menampilkan menu untuk mengubah data."""
    print("\nUbah Data:")
    print("1. Ubah Data Karyawan")
    print("2. Kembali ke Menu Utama")

def tampilkan_menu_hapus_data():
    """Menampilkan menu untuk menghapus data."""
    print("\nHapus Data:")
    print("1. Hapus Data Karyawan")
    print("2. Kembali ke Menu Utama")

def tampilkan_semua_data(data_karyawan): #EROR HANDLING OKE
    """Menampilkan semua data karyawan."""
    if not data_karyawan:
        print("Data karyawan kosong.")
        return

    print("\nDaftar Karyawan:")
    print("-" * 80)
    print("ID\t | Nama \t | Usia\t | Jabatan \t\t | Gaji")
    print("_" *80)
    for karyawan in (data_karyawan):
        print(f"|{karyawan['id']}\t | {karyawan['nama']} \t | {karyawan['usia']} \t | {karyawan['jabatan']} \t\t |{karyawan['gaji']}")

def cari_data_karyawan(data_karyawan):
    """Mencari data karyawan berdasarkan ID."""
    if not data_karyawan:
        print("Data karyawan kosong.")
        return
    id_karyawan = input("Masukkan ID karyawan: ")
    for karyawan in data_karyawan:
        if karyawan["id"] == id_karyawan:
            print("\nDaftar Karyawan")
            print("-" * 80)
            print("|ID\t | Nama\t\t | Usia\t\t | Jabatan \t\t |Gaji")
            print("_" * 80)
            print(f"|{karyawan['id']}\t | {karyawan['nama']} \t | {karyawan['usia']} \t\t | {karyawan['jabatan']}\t\t |{karyawan['gaji']}")
            return
    print("Data karyawan tidak ditemukan.")
def tambah_data_karyawan(data_karyawan):
    """Menambahkan data karyawan baru."""
    id_karyawan = input("Masukkan ID karyawan: ")
    #check Id
    for karyawan in data_karyawan:
        if karyawan["id"] == id_karyawan:
            print("Id Karyawan Sudah Ada !")
            return
        else:
            print()
    nama = input("Masukkan nama karyawan: ")

    while True:
        usia_str = input("Masukkan usia karyawan: ")
        try:
            usia = int(usia_str.split()[0]) #angka sebelum spasi
            break
        except ValueError:
            print("input usia harus berupa angka. Contoh 29")

    jabatan = input("Masukkan jabatan karyawan: ")
    while True:
        gaji_str = input("Masukkan gaji karyawan: ")
        try:
            gaji = int(gaji_str)
            break
        except ValueError:
            print("Gaji harus Berupa angka, Contoh : 5000")
#Append data karyawan
    data_karyawan.append({
        "id": id_karyawan,
        "nama": nama,
        "usia": usia,
        "jabatan": jabatan,
        "gaji": gaji
    })
    print("Data karyawan berhasil ditambahkan.")

def ubah_data_karyawan(data_karyawan):
    """Mengubah data karyawan berdasarkan ID."""
    if not data_karyawan:
        print("Data karyawan kosong.")
        return

    id_karyawan = input("Masukkan ID karyawan: ")
    for karyawan in data_karyawan:
        if karyawan["id"] == id_karyawan:
            print("Data Karyawan:")
            print(karyawan)
            if input("Lanjutkan ubah data? (ya/tidak): ").lower() == "ya":
                kolom = input("Masukkan kolom yang ingin diubah: ")
                nilai_baru = input("Masukkan nilai baru: ")
                karyawan[kolom] = nilai_baru
                print("Data karyawan berhasil diubah.")
            return

    print("Data karyawan tidak ditemukan.")

def hapus_data_karyawan(data_karyawan):

    """Menghapus data karyawan berdasarkan ID."""
    if not data_karyawan:
        print("Data karyawan kosong.")
        return

    id_karyawan = input("Masukkan ID karyawan: ")
    for i, karyawan in enumerate(data_karyawan):
        if karyawan["id"] == id_karyawan:
            print("Data Karyawan:")
            print(karyawan)
            if input("Lanjutkan hapus data? (ya/tidak): ").lower() == "ya":
                del data_karyawan[i]
                print("Data karyawan berhasil dihapus.")
            return

    print("Data karyawan tidak ditemukan.")
# Loop utama program

while True:
    tampilkan_menu_utama()
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        tampilkan_menu_tampilkan_data()
        pilihan_tampilkan_data = input("Masukkan pilihan Anda: ")
        if pilihan_tampilkan_data == "1":
            tampilkan_semua_data(data_karyawan)
        elif pilihan_tampilkan_data == "2":
            cari_data_karyawan(data_karyawan)
        elif pilihan_tampilkan_data == "3":
            pass  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid.")
    elif pilihan == "2":
        tampilkan_menu_tambah_data()
        pilihan_tambah_data = input("Masukkan pilihan Anda: ")
        if pilihan_tambah_data == "1":
            tambah_data_karyawan(data_karyawan)
        elif pilihan_tambah_data == "2":
            pass  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid.")
    elif pilihan == "3":
        tampilkan_menu_ubah_data()
        pilihan_ubah_data = input("Masukkan pilihan Anda: ")
        if pilihan_ubah_data == "1":
            ubah_data_karyawan(data_karyawan)
        elif pilihan_ubah_data == "2":
            pass  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid.")
    elif pilihan == "4":
        tampilkan_menu_hapus_data()
        pilihan_hapus_data = input("Masukkan pilihan Anda: ")
        if pilihan_hapus_data == "1":
            hapus_data_karyawan(data_karyawan)
        elif pilihan_hapus_data == "2":
            pass  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid.")
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")