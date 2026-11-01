# 4.11 MY PIZZAS IS YOUR PIZZAS
# Gunakan program dari latihan 4-1 (pizzas.py).
# Salin list pizza yang sudah dibuat dan beri nama friend_pizzas.
# Tambahkan satu jenis pizza baru ke list asli.
# Tambahkan jenis pizza berbeda ke list friend_pizzas.
# Buktikan bahwa kedua list merupakan list yang berbeda:
# - Tampilkan pesan My favorite pizzas are:, kemudian gunakan for loop untuk menampilkan pizza milikmu.
# - Tampilkan pesan My friend's favorite pizzas are:, kemudian gunakan for loop untuk menampilkan pizza milik temanmu.
# Pastikan setiap pizza baru masuk ke list yang sesuai.

# Membuat daftar pizza favorit
pizzas = ["Pepperoni", "Cheese", "Meat Lovers"]

# Menyalin list pizza
friend_pizzas = pizzas[:]

# Menambahkan pizza ke daftar masing-masing
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