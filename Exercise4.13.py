# 4.13 BUFFET
# Sebuah restoran bergaya prasmanan (buffet) hanya menyediakan lima jenis makanan dasar.
# Pikirkan lima makanan sederhana dan simpan ke dalam sebuah tuple.
# Gunakan for loop untuk menampilkan setiap makanan yang tersedia.
# Coba ubah salah satu elemen tuple dan pastikan Python menolak perubahan tersebut.
# Restoran mengubah menunya dengan mengganti dua jenis makanan.
# Tambahkan satu baris kode untuk menulis ulang tuple dengan menu baru.
# Gunakan for loop untuk menampilkan seluruh makanan pada menu yang telah diperbarui.

# Membuat tuple berisi lima jenis makanan
foods = ("Nasi goreng", "Ayam goreng", "Sate", "Bakso", "Soto")

# Menampilkan menu restoran
print("Menu makanan restoran:")
for food in foods:
    print(food)

# Mencoba mengubah salah satu elemen tuple
foods[0] = "Mie goreng"

# Mengganti menu restoran dengan tuple baru
foods = ("Nasi goreng", "Mie goreng", "Sate", "Rendang", "Soto")

# Menampilkan menu restoran yang baru
print("\nMenu makanan terbaru:")
for food in foods:
    print(food)