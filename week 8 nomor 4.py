from array import array

list_buah = ["Apel", "Mangga", "Jeruk"]
list_buah.append("Anggur")
list_buah.remove("Mangga")  # Perbaikan 1: pop() hanya menerima indeks, bukan nilai
print("List Buah:", list_buah)

arr_nilai = array('f', [85.5, 92.0, 78.5, 90.0])
arr_nilai.append(87.0)
nilai_pertama = arr_nilai[0]
print("Nilai pertama adalah:", nilai_pertama)  # Perbaikan 2: tidak bisa menggabungkan string + float

arr_nilai[2] = 80.0  # Perbaikan 3: array type 'f' hanya menerima angka float, bukan string
print("Array Nilai:", arr_nilai)