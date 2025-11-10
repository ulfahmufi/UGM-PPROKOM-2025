# main.py
import aritmatika
print("=== PROGRAM OPERASI MATEMATIKA ===")
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
print("Hasil Penjumlahan: ", aritmatika.penjumlahan(a, b))
print("Hasil Pengurangan: ", aritmatika.pengurangan(a, b))
print("Hasil Perkalian: ", aritmatika.perkalian(a, b))
print("Hasil Pembagian: ", aritmatika.pembagian(a, b))
print("Hasil Modulo: ", aritmatika.modulo(a, b))
print("Hasil Pangkat: ", aritmatika.pangkat(a, b))