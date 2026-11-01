# 3.8 SEEING THE WORLD

# Membuat daftar tempat yang ingin dikunjungi
places = ["Jepang", "Swiss", "Turki", "Korea Selatan", "Mesir", "Italia"]

# Menampilkan daftar dalam urutan awal
print("Urutan awal:")
print(places)

# Mengurutkan secara alfabetis tanpa mengubah list asli
print("\nUrutan alfabetis:")
print(sorted(places))

# Memastikan urutan list asli tidak berubah
print("\nUrutan asli:")
print(places)

# Mengurutkan secara alfabetis terbalik tanpa mengubah list asli
print("\nUrutan alfabetis terbalik:")
print(sorted(places, reverse=True))

# Memastikan urutan list asli tetap sama
print("\nUrutan asli:")
print(places)

# Membalik urutan list
places.reverse()
print("\nSetelah menggunakan reverse() pertama:")
print(places)

# Mengembalikan urutan list seperti semula
places.reverse()
print("\nSetelah menggunakan reverse() kedua:")
print(places)

# Mengurutkan list secara alfabetis
places.sort()
print("\nSetelah menggunakan sort() alfabetis:")
print(places)

# Mengurutkan list secara alfabetis terbalik
places.sort(reverse=True)
print("\nSetelah menggunakan sort() terbalik:")
print(places)