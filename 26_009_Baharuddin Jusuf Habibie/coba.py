daftarBuku = ['audit', 'tata kelola', 'si kancil']

nama = input("masukkan nama anda: ")
umur = int(input("masukkan umur anda: "))
statusAktif = input("apakah status keanggotaan anda aktif (y/n): ").lower() == 'y'

print("===Koleksi Buku===")
print("0", daftarBuku[0])
print("1", daftarBuku[1])
print("2", daftarBuku[2])

pilihan1 = int (input("pilih buku ke 1: "))

syaratUmur = statusAktif and umur >= 17

hariSekarang = 0
lamaPinjam = 1
batasPengembalian = hariSekarang + lamaPinjam

print ("==hasil peminjaman==")
if not syaratUmur:
    print(f"maaf {nama}, peminjaman ditolak")
    if not statusAktif:
        print(f"maaf {nama}, status keanggotaan anda tidak aktif")
else:
    bukuDipinjam = daftarBuku[pilihan1]
    print(f"selamat {nama}, peminjaman buku {bukuDipinjam}")
    print(f"lama peminjaman buku adalah {lamaPinjam} hari")
    print(f"batas pengembalian buku adalah {batasPengembalian}")
    
    