# 6.1 PERSON
# Buat sebuah dictionary untuk menyimpan informasi seseorang yang kamu kenal.
# Simpan empat informasi:
# - Nama depan (first name).
# - Nama belakang (last name).
# - Umur (age).
# - Kota tempat tinggal (city).
# Gunakan key first_name, last_name, age, dan city.
# Tampilkan setiap informasi yang tersimpan dalam dictionary.

# Membuat dictionary berisi informasi seseorang
person = {
    "first_name": "Muhammad",
    "last_name": "Yasir",
    "age": 19,
    "city": "Surakarta"
}

# Menampilkan informasi seseorang
print("Informasi Seseorang")
print(f"Nama depan: {person['first_name']}")
print(f"Nama belakang: {person['last_name']}")
print(f"Umur: {person['age']} tahun")
print(f"Kota: {person['city']}")