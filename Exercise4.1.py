# 4.1 PIZZAS
# Pikirkan minimal tiga jenis pizza favoritmu.
# 1. Simpan nama-nama pizza tersebut ke dalam sebuah list.
# 2. Gunakan for loop untuk menampilkan nama setiap pizza.
# 3. Modifikasi for loop agar menampilkan kalimat menggunakan nama pizza, misalnya "Saya suka pizza pepperoni."
# 4. Tambahkan satu kalimat di akhir program, di luar for loop, yang menyatakan seberapa kamu menyukai pizza.
# 5. Output harus terdiri dari minimal tiga baris tentang jenis pizza yang kamu sukai, kemudian satu kalimat tambahan.

# Membuat daftar pizza favorit
pizzas = ["Pepperoni", "Cheese", "Meat Lovers"]

# Menampilkan nama setiap pizza
for pizza in pizzas:
    print(pizza)

# Menampilkan kalimat tentang setiap pizza
for pizza in pizzas:
    print(f"Saya suka pizza {pizza}.")

# Menampilkan kalimat di luar perulangan
print("Saya benar-benar menyukai pizza!")