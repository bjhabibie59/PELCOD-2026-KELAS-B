nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")
tinggi = input("Masukkan tinggi: ")
angkaFavorit = int(input("Masukkan angka favorit: "))

print("\nData Anda:")
print("Nama :", nama)
print("Umur :", umur)
print("Tinggi :", tinggi)
print("Angka Favorit :", angkaFavorit)

hargaPensil = 2000
hargaBuku = 5000
print("\nHarga 1 pensil = Rp.", hargaPensil)
print("Harga 1 Buku = Rp.", hargaBuku)

print("4 pensil = Rp.", hargaPensil * 4)
print("2 buku = Rp.", hargaBuku * 2)

totalBelanja = hargaPensil * 4 + hargaBuku * 2
print("Total belanja = Rp.", totalBelanja)

print("\nKondisi Angka Favorit")
if angkaFavorit % 2 == 0:
    print("Angka favorit adalah bilangan genap")
else:
    print("Angka favorit adalah bilangan ganjil")

mahasiswa_aktif = input("Masukkan nama mahasiswa: ")