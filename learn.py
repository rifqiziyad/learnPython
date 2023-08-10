import module
from module import kali, inputData

# komentar 1 baris

"""
komentar lebih dari 1 baris
"""

# tipe data Boolean

print(True)

# tipe data String
print("Ayo belajar Python")
print('Belajar Python Sangat Mudah')

# tipe data Integer
print(20)

# tipe data Float
print(3.14)

# tipe data Hexadecimal
# print(9a)

# tipe data Complex
print(5j)

# tipe data List
print([1, 2, 3, 4, 5])
print(["satu", "dua", "tiga"])

# tipe data Tuple
print((1, 2, 3, 4, 5))
print(("satu", "dua", "tiga"))

# tipe data Dictionary
print({"nama": "Budi", 'umur': 20})
# tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama": "Andi", 'umur': 21}  # proses inisialisasi variabel biodata
print(biodata)  # proses pencetakan variabel biodata yang berisi tipe data Dictionary
# fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'> yang berarti dict adalah tipe data dictionary
print(type(biodata))


# proses memasukan data ke dalam variabel
nama = "John Doe"
# proses mencetak variabel
print(nama)

# nilai dan tipe data dalam variabel dapat diubah
umur = 20  # nilai awal
print(umur)  # mencetak nilai umur
type(umur)  # mengecek tipe data umur
umur = "dua puluh satu"  # nilai setelah diubah
print(umur)  # mencetak nilai umur
type(umur)  # mengecek tipe data umur

namaDepan = "Budi"
namaBelakang = "Susanto"
nama = namaDepan + " " + namaBelakang
umur = 22
hobi = "Berenang"
print("Biodata\n", nama, "\n", umur, "\n", hobi)

# contoh variabel lainya
inivariabel = "Halo"
ini_juga_variabel = "Hai"
_inivariabeljuga = "Hi"
inivariabel222 = "Bye"

panjang = 10
lebar = 5
luas = panjang * lebar
print(luas)


# scope variabel

angka = 20
nama = "Rifqi"


def ubah(nilai_baru, nama_baru):
    global angka  # agar bisa mengakses variabel global
    global nama

    angka = nilai_baru
    nama = nama_baru


print(f"sebelum {angka, nama}")
ubah(10, "Ziyad")
print(f"sesudah {angka, nama}")

# import statment

hasil = module.kali("halo", 10)
print(hasil)

print(inputData("Rifqi", "20-22-01"))
