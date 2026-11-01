# 7.3 MULTIPLE OF TEN
# Minta pengguna memasukkan sebuah angka.
# Periksa apakah angka tersebut merupakan kelipatan 10.
# Jika iya, tampilkan pesan bahwa angka tersebut merupakan kelipatan 10.
# Jika tidak, tampilkan pesan bahwa angka tersebut bukan kelipatan 10.

# Meminta pengguna memasukkan sebuah angka
number = int(input("Masukkan sebuah angka: "))

# Memeriksa apakah angka merupakan kelipatan 10
if number % 10 == 0:
    print(f"{number} merupakan kelipatan 10.")
else:
    print(f"{number} bukan kelipatan 10.")