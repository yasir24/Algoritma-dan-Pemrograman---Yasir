# 7.5 MOVIE TICKETS
# Buat program yang menanyakan umur pengguna dan menentukan harga tiket bioskop berdasarkan ketentuan:
# Umur	Harga tiket
# Di bawah 3 tahun	Gratis
# 3–12 tahun	$10
# Di atas 12 tahun	$15
# Program harus terus meminta umur pengguna menggunakan perulangan.

# Memulai perulangan untuk menghitung harga tiket
while True:
    age = input("Masukkan umur Anda (ketik quit untuk selesai): ")

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        print("Harga tiket: Gratis")
    elif age <= 12:
        print("Harga tiket: $10")
    else:
        print("Harga tiket: $15")