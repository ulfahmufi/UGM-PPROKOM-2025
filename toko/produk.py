# produk.py

produk = [
    ("Keyboard", 150000),
    ("Mouse", 80000),
    ("Flashdisk", 60000)
]
def tampilkan_produk():
    print("\n=== DAFTAR PRODUK ===")
    for i, item in enumerate(produk, start=1):
        print(f"{i}. {item[0]} . Rp{item[1]}")