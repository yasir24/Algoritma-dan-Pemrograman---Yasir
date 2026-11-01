# 6.7 PEOPLE
# Gunakan kembali dictionary dari latihan 6-1.
# Buat dua dictionary baru yang mewakili dua orang berbeda.
# Simpan ketiga dictionary tersebut dalam sebuah list bernama people.
# Gunakan perulangan untuk menampilkan seluruh informasi setiap orang.

# Membuat dictionary berisi informasi tiga orang
person_1 = {
    "first_name": "Muhammad",
    "last_name": "Yasir",
    "age": 19,
    "city": "Surakarta"
}

person_2 = {
    "first_name": "Windah",
    "last_name": "Basudara",
    "age": 31,
    "city": "Manado"
}

person_3 = {
    "first_name": "Pria",
    "last_name": "Solo",
    "age": 45,
    "city": "Solo"
}

# Menyimpan ketiga dictionary dalam sebuah list
people = [person_1, person_2, person_3]

# Menampilkan informasi setiap orang
for person in people:
    print(f"\nNama: {person['first_name']} {person['last_name']}")
    print(f"Umur: {person['age']} tahun")
    print(f"Kota: {person['city']}")