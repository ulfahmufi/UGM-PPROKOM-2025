# data_mhs.py
daftar_mhs = []
def tambah_data(nama, nim):
    daftar_mhs.append((nama, nim))
def tampilkan_data():
    for i, data in enumerate(daftar_mhs, start=1):
        print(f"{i}. {data[0]} ({data[1]})")