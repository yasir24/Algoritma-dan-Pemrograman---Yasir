# 4.5 Summing a Millon
# Buat list berisi angka 1 sampai 1.000.000.
# Gunakan min() untuk memastikan angka terkecil adalah 1.
# Gunakan max() untuk memastikan angka terbesar adalah 1.000.000.
# Gunakan sum() untuk menjumlahkan seluruh angka dalam list.

# Membuat list angka 1 sampai 1.000.000
numbers = list(range(1, 1000001))

# Menampilkan angka terkecil
print("Angka terkecil:", min(numbers))

# Menampilkan angka terbesar
print("Angka terbesar:", max(numbers))

# Menjumlahkan seluruh angka
print("Jumlah seluruh angka:", sum(numbers))