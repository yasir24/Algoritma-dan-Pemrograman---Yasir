# 3.10 EVERY FUNCTION
# menggunakan beberapa fungsi dan metode list

# Membuat daftar gunung di Indonesia
mountains = ["Semeru", "Merapi", "Rinjani", "Bromo", "Kerinci"]

# 1. Menampilkan list
print("Daftar gunung:")
print(mountains)

# 2. Mengakses elemen berdasarkan indeks
print("\nGunung pertama:")
print(mountains[0])

# 3. Mengubah elemen dalam list
mountains[1] = "Merbabu"
print("\nSetelah mengganti elemen:")
print(mountains)

# 4. Menambahkan elemen menggunakan append()
mountains.append("Slamet")
print("\nSetelah menggunakan append():")
print(mountains)

# 5. Menambahkan elemen menggunakan insert()
mountains.insert(0, "Pangrango")
print("\nSetelah menggunakan insert():")
print(mountains)

# 6. Menghapus elemen menggunakan del
del mountains[0]
print("\nSetelah menggunakan del:")
print(mountains)

# 7. Menghapus elemen menggunakan pop()
popped_mountain = mountains.pop()
print("\nGunung yang dihapus:", popped_mountain)
print(mountains)

# 8. Menghapus elemen berdasarkan nilai menggunakan remove()
mountains.remove("Bromo")
print("\nSetelah menggunakan remove():")
print(mountains)

# 9. Mengurutkan list menggunakan sorted()
print("\nUrutan alfabetis:")
print(sorted(mountains))

# 10. Membalik urutan menggunakan reverse()
mountains.reverse()
print("\nSetelah menggunakan reverse():")
print(mountains)

# 11. Mengurutkan list menggunakan sort()
mountains.sort()
print("\nSetelah menggunakan sort():")
print(mountains)

# 12. Menghitung jumlah elemen menggunakan len()
print("\nJumlah gunung:", len(mountains))