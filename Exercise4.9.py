# 4.9 CUBES COMPREHENSION
# Gunakan list comprehension untuk membuat list yang berisi hasil pangkat tiga dari 10 bilangan pertama.
# Tidak perlu menggunakan for loop terpisah untuk mengisi list.

# Membuat list pangkat tiga menggunakan list comprehension
cubes = [number ** 3 for number in range(1, 11)]

# Menampilkan hasil pangkat tiga
for cube in cubes:
    print(cube)