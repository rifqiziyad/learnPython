import sains
from sains.matematika import scientific

hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 45)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = sains.fisika.gaya(10, 9.8)
print(f"hasil fisika = {hasil_fisika}")

hasil_kali = sains.matematika.kali(1, 3, 4, 5, 6)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = scientific.pangkat(3)
print(f"hasil pangkat 3 = {pangkat_3(5)}")

# from sains import *

# hasil_tambah = matematika.basic.tambah(1,2,3,4,45)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_pisika = pisika.gaya(10,9.8)
# print(f"hasil pisika = {hasil_pisika}")

# hasil_kali = matematika.basic.kali(1,3,4,5,6)
# print(f"hasil kali = {hasil_kali}")


# Tutorial membaca file eksternal
''' 
- membaca file eksternal bisa menggunakan fungsi "open" dan "with"
- ketika membuka file, harus menutupnya kembali
- pada fungsi "with" file akan otomatis tertutup, tanpa harus menjalankan funsi close()
'''

print(3*"=", " Membaca file txt ", 3*"=")
file = open("data.txt", mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

# baca seluruh file
print(file.read())

# baca per baris
# print(file.readline(),end="") # baca baris pertama
# print(file.readline(),end="") # baca baris kedua

# baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah diclose : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")


# salah satu teknik membuka file di python

print("\n", 3*"=", " Membaca file txt dengan with", 3*"=")

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"apakah file sudah diclose : {file.closed}")

print(f"apakah file sudah diclose : {file.closed}")
