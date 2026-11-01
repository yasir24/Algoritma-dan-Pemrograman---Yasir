# 4.10 SLICES
# Gunakan salah satu program yang sudah dibuat pada bab ini.
# Tambahkan beberapa baris kode di akhir program untuk melakukan tiga hal:
# - Tampilkan pesan The first three items in the list are:, kemudian tampilkan tiga elemen pertama menggunakan slicing.
# - Tampilkan pesan Three items from the middle of the list are:, kemudian tampilkan tiga elemen dari bagian tengah list menggunakan slicing.
# - Tampilkan pesan The last three items in the list are:, kemudian tampilkan tiga elemen terakhir menggunakan slicing.

# Membuat daftar gunung
mountains = ["Semeru", "Merapi", "Rinjani", "Bromo", "Kerinci", "Slamet"]

# Menampilkan tiga elemen pertama
print("Tiga elemen pertama dalam daftar:")
print(mountains[:3])

# Menampilkan tiga elemen dari bagian tengah
print("\nTiga elemen dari bagian tengah daftar:")
print(mountains[2:5])

# Menampilkan tiga elemen terakhir
print("\nTiga elemen terakhir dalam daftar:")
print(mountains[-3:])