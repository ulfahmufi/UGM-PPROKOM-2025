import NumPy as np

A = np.array([[2, 4, 6],
              [1, 3, 5]])

B = np.array([[1, 1, 1],
              [2, 2, 2]])
tambah = np.add(A, B)
kurang = np.substract(A, B)

print("Penjumlahan Matriks A + B:\n", tambah)
print("Pengurangan Matriks A - B:\n", kurang)