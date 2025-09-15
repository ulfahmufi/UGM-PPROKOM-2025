# Menghitung Rata-Rata

jumlah = int(input("Masukkan jumlah nilai:"))
total = 0

for i in range(jumlah):
    nilai = float(input(f"Masukkan nilai ke-{i+1}:"))
    total += nilai

rata_rata = total / jumlah
print(f"Rata-rata dari {jumlah} nilai adalah: {rata_rata}")