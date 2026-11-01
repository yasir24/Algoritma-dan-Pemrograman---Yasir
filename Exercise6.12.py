# 6.12 EXTENSION
# Pilih salah satu program dari Chapter 6, kemudian kembangkan dengan cara:
# - Menambahkan key dan value baru.
# - Mengubah konteks program.
#- Memperbaiki format output agar lebih menarik.

# Membuat dictionary berisi informasi tiga orang
person_1 = {
    "first_name": "Muhammad",
    "last_name": "Yasir",
    "age": 19,
    "city": "Surakarta",
    "occupation": "Mahasiswa",
    "hobby": "Ngegym sambil dengerin musik"
}

person_2 = {
    "first_name": "Narasti",
    "last_name": "Surendra",
    "age": 19,
    "city": "Wonogiri",
    "occupation": "Mahasiswa",
    "hobby": "Nonton drakor"
}

person_3 = {
    "first_name": "Andi",
    "last_name": "Pratama",
    "age": 21,
    "city": "Semarang",
    "occupation": "Karyawan",
    "hobby": "Bermain musik"
}

# Menyimpan seluruh informasi dalam sebuah list
people = [person_1, person_2, person_3]

# Menampilkan informasi setiap orang
print("DAFTAR PROFIL PENGGUNA")
print("======================")

for person in people:
    print(f"\nNama: {person['first_name']} {person['last_name']}")
    print(f"Umur: {person['age']} tahun")
    print(f"Kota: {person['city']}")
    print(f"Pekerjaan: {person['occupation']}")
    print(f"Hobi: {person['hobby']}")
    print("----------------------")