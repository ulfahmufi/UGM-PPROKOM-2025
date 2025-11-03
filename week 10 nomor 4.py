# Program Kalkulator Matematika Sederhana

import math  # untuk operasi akar kuadrat

# Meminta input identitas dari pengguna
print("=== PROGRAM KALKULATOR MATEMATIKA SEDERHANA ===")
nama = input("Masukkan Nama Anda: ")
nim = input("Masukkan NIM Anda: ")

# Fungsi-fungsi operasi
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return "Error: Pembagi tidak boleh nol!"
    else:
        return a / b

def perpangkatan(a, b):
    return a ** b

def akar_kuadrat(a):
    if a < 0:
        return "Error: Tidak dapat menghitung akar bilangan negatif!"
    else:
        return math.sqrt(a)

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n======= MENU KALKULATOR =======")
    print("[1] Penjumlahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")
    print("[5] Perpangkatan")
    print("[6] Akar Kuadrat")
    print("[7] Keluar")

# Program utama (main loop)
while True:
    show_menu()
    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil =", penjumlahan(a, b))
    elif pilihan == "2":
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil =", pengurangan(a, b))
    elif pilihan == "3":
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil =", perkalian(a, b))
    elif pilihan == "4":
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil =", pembagian(a, b))
    elif pilihan == "5":
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan pangkat: "))
        print("Hasil =", perpangkatan(a, b))
    elif pilihan == "6":
        a = float(input("Masukkan bilangan: "))
        print("Hasil =", akar_kuadrat(a))
    elif pilihan == "7":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
