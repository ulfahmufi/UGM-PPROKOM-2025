buah_buahan = {
    "Apel": 15000,
    "Jeruk": 10000,
    "Anggur": 25000
}

# Tampilkan Harga Jeruk
print("Harga Jeruk:", buah_buahan["Jeruk"])

# Tampilkan Mangga
buah_buahan["Mangga"] = 12000
print("Dictionary buah buahan terbaru:", buah_buahan)

# Perbarui Harga Anggur
buah_buahan["Anggur"] = 20000
print("Dictionary buah buahan terbaru:", buah_buahan)

#Hapus Buah Jeruk
del buah_buahan["Jeruk"]
print("Dictionary buah buahan terbaru:", buah_buahan)