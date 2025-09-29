print("\nDictionary Nilai Mahasiswa:")
nilai_mahasiswa = {
    "Aba": 85
    "Abi": 90,
    "Abu": 78
}
print(nilai_mahasiswa)

print("\nMenambah Nilai Abe:")
nilai_mahasisswa.update("Abe": 88)
print(nilai_mahasiswa)

print("\nMengupdate Nilai Abu:")
nilai_mahasiswa[0] = 87
print(nilai_mahasiswa)

print("\nMencetak Semua Nila:i")
for nama, nilai in nilai_mahasiswa:
    print(f"Nilai {nama} adalah {nilai}")