# capstone1.py
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
def tampilkan_menu_utama():
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
    print("_" * 80)
    print("| ID | Nama          | Usia | Jabatan      | Gaji     |")
    print("_" * 80)
    for karyawan in (data_karyawan):
        print(f"| {karyawan['id']:<3} | {karyawan['nama']:<12} | {karyawan['usia']:<4} | {karyawan['jabatan']:<12} | {karyawan['gaji']:>8} | ")

def cari_data_karyawan(data_karyawan):
    """Mencari data karyawan berdasarkan ID."""
    if not data_karyawan:
            print("Data karyawan kosong.")
            return
    id_karyawan = input("Masukkan ID karyawan: ").strip().lower()
    karyawan_ditemukan = False
    for karyawan in data_karyawan:
        if karyawan["id"] == id_karyawan:
            print("\nDaftar Karyawan")
            print("_" * 80)
            print("| ID | Nama          | Usia | Jabatan      | Gaji     |")
            print("_" * 80)
            print(f"| {karyawan['id']:<3} | {karyawan['nama']:<12} | {karyawan['usia']:<4} | {karyawan['jabatan']:<12} | {karyawan['gaji']:>8} | ")
            karyawan_ditemukan = True
            break
    if not karyawan_ditemukan:
        print("Data karyawan tidak ditemukan.")
def tambah_data_karyawan(data_karyawan):
    """Menambahkan data karyawan baru."""
    tampilkan_semua_data(data_karyawan)
    id_karyawan = input("Masukkan ID karyawan: ").strip()
    #Check ID
    if any(karyawan["id"] == id_karyawan for karyawan in data_karyawan):
        print("ID karyawan sudah ada.")
        return

    nama = input("Masukkan nama karyawan: ").strip().capitalize()

        #Check Umur
    while True:
        usia_str = input("Masukkan usia karyawan: ")
        try:
            usia = int(usia_str)
            if 17 <= usia <= 45:
                break
            else:
                print("Usia harus antara 17-45")
        except ValueError:
            print("input usia harus berupa angka. Contoh 29")

        #Check Jabatan
    while True:
        jabatan = input("Masukkan jabatan karyawan: ").strip().capitalize()
        if jabatan in ["Manager", "Staff", "Supervisor"]:
            break
        else:
            print("Jabatan harus Manager, Staff, atau Supervisor")
            
        #Check Gaji
    while True:
        gaji_str = input("Masukkan gaji karyawan: ")
        try:
            gaji = int(gaji_str)
            if gaji >= 4500000:
                break
            else:
                print("Gaji harus lebih dari 4500000")
        except ValueError:
            print("Gaji harus Berupa angka, Contoh : 4500000")

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
    tampilkan_semua_data(data_karyawan)
    id_karyawan = input("Masukkan ID karyawan: ")
    if not id_karyawan.isdigit():
        print("ID harus berupa angka.")
        return
    for karyawan in data_karyawan:
        if karyawan["id"] == id_karyawan:
            print("Data Karyawan:")
            print(karyawan)
            if input("Lanjutkan ubah data? (ya/tidak): ").lower() == "ya":
                kolom = input("Masukkan kolom yang ingin diubah: ")
                if kolom not in karyawan:
                    print("Kolom tidak valid.")
                    return
                nilai_baru = input("Masukkan nilai baru: ").capitalize()
                karyawan[kolom] = nilai_baru
                print("Data karyawan berhasil diubah.")
            else:
                print("Data karyawan tidak diubah.")
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
# Menampilkan menu utama
# Loop utama#
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
            pass     # Kembali ke menu utama
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