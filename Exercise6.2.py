# 6.2 FAVORITE NUMBERS
# Buat dictionary untuk menyimpan angka favorit lima orang.
# Gunakan nama orang sebagai key.
# Gunakan angka favorit masing-masing sebagai value.
# Tampilkan nama setiap orang beserta angka favoritnya.

# Membuat dictionary berisi angka favorit lima orang
favorite_numbers = {
    "budi": 7,
    "windah": 12,
    "miook": 5,
    "yasir": 10,
    "pria solo": 25
}

# Menampilkan nama dan angka favorit setiap orang
print("ANGKA FAVORIT TEMAN")

for name, number in favorite_numbers.items():
    print(f"{name.title()} menyukai angka {number}.")