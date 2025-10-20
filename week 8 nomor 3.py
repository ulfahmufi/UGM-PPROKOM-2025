from array import array

def main():
    # Membuat array integer kosong
    data = array('i', [])

    print("Masukkan 5 bilangan bulat:")
    for i in range(5):
        nilai = int(input(f"Nilai ke-{i+1}: "))
        data.append(nilai)

    # Menampilkan array dan panjangnya
    print("\nIsi array:", data.tolist())
    print("Panjang array:", len(data))

    # Menghitung jumlah total dan rata-rata
    total = sum(data)
    rata_rata = total / len(data)

    print("Jumlah total elemen:", total)
    print("Nilai rata-rata:", rata_rata)

if __name__ == "__main__":
    main()