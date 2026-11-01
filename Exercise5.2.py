# 5.2 MORE CONDITIONAL TESTS
# Buat pengujian kondisi tambahan di file conditional_tests.py. Kamu harus memiliki minimal satu hasil True dan satu hasil False untuk setiap kategori berikut:
# 1. Pengujian kesamaan (==) dan ketidaksamaan (!=) pada string.
# 2. Pengujian menggunakan metode .lower().
# 3. Pengujian numerik yang melibatkan:
#   - Sama dengan (==).
#   - Tidak sama dengan (!=).
#   - Lebih besar (>).
#   - Lebih kecil (<).
#   - Lebih besar atau sama dengan (>=).
#   - Lebih kecil atau sama dengan (<=).
# 4. Pengujian menggunakan operator and dan or.
# 5. Menguji apakah suatu elemen terdapat dalam list (in).
# 6. Menguji apakah suatu elemen tidak terdapat dalam list (not in).

# Membuat variabel nama
name = "Yasir"

# Pengujian kesamaan string
print("Apakah nama == 'Yasir'? Prediksi: True.")
print(name == "Yasir")

print("\nApakah nama == 'Azhar'? Prediksi: False.")
print(name == "Azhar")

# Pengujian ketidaksamaan string
print("\nApakah nama != 'Azhar'? Prediksi: True.")
print(name != "Azhar")

print("\nApakah nama != 'Yasir'? Prediksi: False.")
print(name != "Yasir")

# Membuat variabel bahasa
language = "PYTHON"

# Mengubah string menjadi huruf kecil sebelum dibandingkan
print("\nApakah language.lower() == 'python'? Prediksi: True.")
print(language.lower() == "python")

print("\nApakah language.lower() == 'java'? Prediksi: False.")
print(language.lower() == "java")

# Membuat variabel angka
number = 10

# Pengujian sama dengan
print("\nApakah number == 10? Prediksi: True.")
print(number == 10)

print("\nApakah number == 5? Prediksi: False.")
print(number == 5)

# Pengujian tidak sama dengan
print("\nApakah number != 5? Prediksi: True.")
print(number != 5)

print("\nApakah number != 10? Prediksi: False.")
print(number != 10)

# Pengujian lebih besar
print("\nApakah number > 5? Prediksi: True.")
print(number > 5)

print("\nApakah number > 15? Prediksi: False.")
print(number > 15)

# Pengujian lebih kecil
print("\nApakah number < 15? Prediksi: True.")
print(number < 15)

print("\nApakah number < 5? Prediksi: False.")
print(number < 5)

# Pengujian lebih besar atau sama dengan
print("\nApakah number >= 10? Prediksi: True.")
print(number >= 10)

print("\nApakah number >= 15? Prediksi: False.")
print(number >= 15)

# Pengujian lebih kecil atau sama dengan
print("\nApakah number <= 10? Prediksi: True.")
print(number <= 10)

print("\nApakah number <= 5? Prediksi: False.")
print(number <= 5)

# Membuat variabel umur
age = 19

# Pengujian menggunakan and
print("\nApakah age > 17 dan age < 25? Prediksi: True.")
print(age > 17 and age < 25)

print("\nApakah age > 20 dan age < 25? Prediksi: False.")
print(age > 20 and age < 25)

# Pengujian menggunakan or
print("\nApakah age < 18 atau age == 19? Prediksi: True.")
print(age < 18 or age == 19)

print("\nApakah age < 18 atau age > 25? Prediksi: False.")
print(age < 18 or age > 25)

# Membuat daftar makanan
foods = ["Nasi goreng", "Mie ayam", "Sate"]

# Menguji apakah item terdapat dalam list
print("\nApakah 'Sate' ada dalam list? Prediksi: True.")
print("Sate" in foods)

print("\nApakah 'Bakso' ada dalam list? Prediksi: False.")
print("Bakso" in foods)

# Menguji apakah item tidak terdapat dalam list
print("\nApakah 'Bakso' tidak ada dalam list? Prediksi: True.")
print("Bakso" not in foods)

print("\nApakah 'Nasi goreng' tidak ada dalam list? Prediksi: False.")
print("Nasi goreng" not in foods)