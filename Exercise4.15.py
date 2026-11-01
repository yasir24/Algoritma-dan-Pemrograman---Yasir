# 4.15 CODE REVIEW
# Pilih tiga program yang sudah kamu buat pada Bab 4, kemudian modifikasi setiap program agar sesuai dengan PEP 8.
# Ketentuan yang harus dipenuhi:
# 1. Gunakan empat spasi untuk setiap tingkat indentasi.
#   - Atur editor agar tombol TAB menghasilkan empat spasi.
# 2. Gunakan kurang dari 80 karakter pada setiap baris.
#   - Atur editor agar menampilkan garis vertikal pada posisi karakter ke-80.
# 3. Jangan menggunakan terlalu banyak baris kosong dalam file program.
# Tiga program yang akan kita rapikan:
# - pizzas.py (latihan 4-1)
# - cubes.py (latihan 4-8)
# - my_pizzas.py (latihan 4-11)

# Membuat daftar pizza favorit
pizzas = ["Pepperoni", "Cheese", "Meat Lovers"]

# Menampilkan setiap pizza
for pizza in pizzas:
    print(f"Saya suka pizza {pizza}.")

# Menampilkan kalimat penutup
print("Saya benar-benar menyukai pizza!")

# Membuat list kosong
cubes = []

# Menghitung pangkat tiga angka 1 sampai 10
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# Menampilkan hasil pangkat tiga
for cube in cubes:
    print(cube)

# Membuat daftar pizza favorit saya
pizzas = ["Pepperoni", "Cheese", "Meat Lovers"]

# Menyalin daftar pizza
friend_pizzas = pizzas[:]

# Menambahkan pizza ke masing-masing daftar
pizzas.append("Hawaiian")
friend_pizzas.append("Chicken")

# Menampilkan pizza favorit saya
print("Pizza favorit saya:")
for pizza in pizzas:
    print(pizza)

# Menampilkan pizza favorit teman saya
print("\nPizza favorit teman saya:")
for pizza in friend_pizzas:
    print(pizza)