# transaksi.py

def hitung_total(harga, jumlah):
    return harga * jumlah
def hitung_diskon(total_harga):
    # contoh: diskon 10% jika total di atas 300000
    if total_harga > 300000:
        return total_harga * 0.10
    else:
        return 0