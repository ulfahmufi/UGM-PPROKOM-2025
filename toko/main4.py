# main.py

import produk
import transaksi

print("=== APLIKASI PENJUALAN TOKO PYTHON ===")
while True:
    produk.tampilkan_produk()
    pilih = int(input("Pilih produk (nomor): "))
    jumlah = int(input("Masukkan jumlah beli: "))

    # Ambil data produk
    nama, harga = produk.produk[pilih - 1]
 
    # Hitung total dan diskon
    total = transaksi.hitung_total(harga, jumlah)
    diskon = transaksi.hitung_diskon(total)
    total_bayar = total - diskon
 
    # Output struk
    print("\n=== STRUK PEMBAYARAN ===")
    print(f"Produk       : {nama}")
    print(f"Harga Satuan : Rp{harga}")
    print(f"Jumlah Beli  : {jumlah}")
    print(f"Total Harga  : Rp{total}")
    print(f"Diskon       : Rp{diskon}")
    print(f"Total Bayar  : Rp{total_bayar}")

    ulang = input("\nApakah ingin belanja lagi? (y/n): ")
    if ulang.lower() != "y":
        print("Terima kasih telah berbelanja.")
        break