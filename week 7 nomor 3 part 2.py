print("\nDictionary Nilai Mahasiswa:")
nilai_mahasiswa = {
    "Aba": 85  #kurang koma
    "Abi": 90,
    "Abu": 78
}
print(nilai_mahasiswa)

print("\nMenambah Nilai Abe:")
nilai_mahasisswa.update("Abe": 88)  #update harus menggunakan tanda kurung dan kurung kurawal di dalamnya
print(nilai_mahasiswa)

print("\nMengupdate Nilai Abu:")
nilai_mahasiswa[0] = 87
print(nilai_mahasiswa)

print("\nMencetak Semua Nila:i")
for nama, nilai in nilai_mahasiswa:  #kurang .items() untuk mengambil pasangan key dan value
    print(f"Nilai {nama} adalah {nilai}")