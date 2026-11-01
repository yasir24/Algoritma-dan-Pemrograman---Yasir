# 6.8 PETS
# Buat beberapa dictionary yang mewakili hewan peliharaan berbeda.
# Setiap dictionary harus memiliki informasi jenis hewan dan nama pemilik.
# Simpan seluruh dictionary dalam list bernama pets.
# Gunakan perulangan untuk menampilkan seluruh informasi hewan.

# Membuat dictionary untuk setiap hewan peliharaan
pet_1 = {
    "animal": "kucing",
    "owner": "Yasir"
}

pet_2 = {
    "animal": "Nomie",
    "owner": "Aren"
}

pet_3 = {
    "animal": "Kucing",
    "owner": "Mama Yiba"
}

pet_4 = {
    "animal": "burung",
    "owner": "Dina"
}

# Menyimpan seluruh hewan dalam sebuah list
pets = [pet_1, pet_2, pet_3, pet_4]

# Menampilkan informasi setiap hewan
for pet in pets:
    print(f"\nJenis hewan: {pet['animal'].title()}")
    print(f"Nama pemilik: {pet['owner']}")