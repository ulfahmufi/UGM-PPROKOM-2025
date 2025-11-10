# main.py
import konversi_suhu
print("=== PROGRAM KONVERSI SUHU ===")
nilai = float(input("Masukkan nilai suhu: "))
asal = input("Masukkan satuan asal (C/F/K): ").upper()
tujuan = input("Konversi ke (C/F/K): ").upper()

if asal == "C" and tujuan == "F":
    print(konversi_suhu.c_to_f(nilai), "F")
elif asal == "C" and tujuan == "K":
    print(konversi_suhu.c_to_k(nilai), "K")
elif asal == "F" and tujuan == "C":
    print(konversi_suhu.f_to_c(nilai), "C")
elif asal == "F" and tujuan == "K":
    print(konversi_suhu.f_to_k(nilai), "K")
elif asal == "K" and tujuan == "C":
    print(konversi_suhu.k_to_c(nilai), "C")
elif asal == "K" and tujuan == "F":
    print(konversi_suhu.k_to_f(nilai), "F")
else:
    print("Satuan tidak valid")