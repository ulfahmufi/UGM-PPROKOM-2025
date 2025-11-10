# main.py
import data_mhs
while True:
    print("\n=== MENU DATA MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Keluar")

    pilih = input("Pilih menu (1-3): ")

    if pilih == "1":
        nama = input("Masukkan nama mahaiswa: ")
        nim = input("Masukkan NIM: ")
        data_mhs.tambah_data(nama, nim)
        print(f"Data mnahasiswa {nama} ({nim}) berhasil ditambahkan!")

    elif pilih == "2":
        print("\n=== DAFTAR MAHASISWA ===")
        data_mhs.tampilkan_data()
    elif pilih == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid")