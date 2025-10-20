def main():
    names = []
    print("Masukkan 5 nama temanmu:")

    # Menyimpan 5 nama ke dalam list
    for i in range(5):
        nama = input(f"Nama ke-{i+1}: ")
        names.append(nama)

    # Menampilkan semua nama beserta indeks
    print("\nDaftar nama dan indeksnya:")
    for i, nama in enumerate(names):
        print(f"[{i}] {nama}")

    # Menanyakan indeks yang ingin diganti
    index = int(input("\nMasukkan indeks nama yang ingin diganti: "))

    # Meminta nama baru sebagai pengganti
    nama_baru = input("Masukkan nama pengganti: ")

    # Melakukan pergantian nama dalam list
    lama = names[index]
    names[index] = nama_baru

    # Menampilkan hasil akhir
    print(f"\nNama '{lama}' telah diganti menjadi '{nama_baru}'.")
    print("Daftar nama terbaru:")
    for i, nama in enumerate(names):
        print(f"[{i}] {nama}")

if __name__ == "__main__":
    main()