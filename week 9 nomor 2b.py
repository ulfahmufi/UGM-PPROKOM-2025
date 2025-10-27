n = int(input("Masukkan ukuran matriks identitas (n): "))

identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print(f"Matriks identitas {n}x{n}:")
for baris in identity:
    print(baris)