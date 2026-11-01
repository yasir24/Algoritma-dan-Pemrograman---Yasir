# 5.1 CONDITIONAL TESTS
# Buat serangkaian pengujian kondisi (conditional tests).
# Tampilkan pernyataan yang menjelaskan setiap pengujian dan prediksi hasilnya.
# Perhatikan hasil yang ditampilkan Python dan pahami alasan setiap kondisi menghasilkan True atau False.
# Buat minimal 10 pengujian:
# - Minimal 5 pengujian menghasilkan True.
# - Minimal 5 pengujian menghasilkan False.

# Membuat variabel mobil
mobil = "subaru"

# Pengujian 1
print("Apakah mobil == 'subaru'? Prediksi: True.")
print(mobil == "subaru")

# Pengujian 2
print("\nApakah mobil == 'toyota'? Prediksi: False.")
print(mobil == "toyota")

# Pengujian 3
print("\nApakah mobil != 'toyota'? Prediksi: True.")
print(mobil != "toyota")

# Pengujian 4
print("\nApakah mobil != 'subaru'? Prediksi: False.")
print(mobil != "subaru")

# Pengujian 5
print("\nApakah mobil.lower() == 'subaru'? Prediksi: True.")
print(mobil.lower() == "subaru")

# Pengujian 6
print("\nApakah mobil == 'SUBARU'? Prediksi: False.")
print(mobil == "SUBARU")

# Pengujian 7
age = 19
print("\nApakah age == 19? Prediksi: True.")
print(age == 19)

# Pengujian 8
print("\nApakah age == 20? Prediksi: False.")
print(age == 20)

# Pengujian 9
print("\nApakah age > 18? Prediksi: True.")
print(age > 18)

# Pengujian 10
print("\nApakah age < 18? Prediksi: False.")
print(age < 18)