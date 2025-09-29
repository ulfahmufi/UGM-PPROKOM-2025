stok_buku = {
    "Harry Potter": 10,
    "Laskar Pelangi": 15,
    "Bumi Manusia": 7,
    "Dilan 1990": 20
}

#Tampilkan Semua Judul Buku
for judul, stok in stok_buku.items():
    print(f"Buku: {judul} - Stok: {stok}")

#Minta Input User untuk Menambah Buku Baru
judul_baru = input("Masukkan judul buku baru: ")
stok_baru = int(input("Masukkan jumlah stok awal: "))
stok_buku[judul_baru] = stok_baru

print(f"Buku {judul_baru} berhasil ditambahkan dengan stok {stok_baru}")
print("Dictionary terbaru:", stok_buku)