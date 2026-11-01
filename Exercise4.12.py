# 4.12 MORE LOOPS
# Semua versi program foods.py pada bagian ini sebelumnya menghindari penggunaan for loop ketika menampilkan list makanan untuk menghemat ruang.
# Pilih salah satu versi program foods.py.
# Buat dua for loop untuk menampilkan setiap list makanan.

# Membuat daftar makanan favorit saya
my_foods = ["Bubur ayam", "Mie ayam", "Sate"]

# Membuat salinan daftar makanan teman saya
friend_foods = my_foods[:]

# Menambahkan makanan ke daftar masing-masing
my_foods.append("Bakso")
friend_foods.append("Rendang")

# Menampilkan makanan favorit saya
print("Makanan favorit saya:")
for food in my_foods:
    print(food)

# Menampilkan makanan favorit teman saya
print("\nMakanan favorit teman saya:")
for food in friend_foods:
    print(food)